import asyncio
from typing import Tuple, Any, List, Optional, Set

import aiohttp
import pandas as pd
import pytz
from pandas import DataFrame, Timestamp
from finclaw.utils.progress_bar import progress_bar

from finclaw.config import logger
from finclaw.data_store.schema import (
    OHCL,
    STOCK_SYMBOL,
    BALANCE_SHEET_V2,
    INCOME_STATEMENT_V2,
    CASHFLOW_STATEMENT_V2,
)
from finclaw.data_store.store import PriceStore
from finclaw.vendor.fmp import fmp_client
import pyarrow as pa

from finclaw.vendor.fmp.fmp_client import get_financials_for
from finclaw.vendor.fmp.models import normalize_names


async def get_symbols(session: aiohttp.ClientSession, market: str) -> pd.DataFrame:
    if market != "TO":
        raise ValueError(f"Market {market} not supported")

    symbols = await fmp_client.get_symbols(session=session)
    df = pd.DataFrame(data=symbols)
    df["mic"] = ""
    df.loc[df["stockExchange"] == "Toronto Stock Exchange", "mic"] = "XTSE"
    df.loc[df["stockExchange"] == "TSXV", "mic"] = "XTSX"
    df = df.rename(
        columns={"symbol": "ticker", "name": "description", "currency": "currency_name"}
    )
    df["type"] = ""
    df["figi"] = ""
    return df[STOCK_SYMBOL.names]


async def get_ohcl_for_symbol(
    session: aiohttp.ClientSession, symbol: str, resolution: str
) -> Optional[pd.DataFrame]:
    ohcl_json = await fmp_client.get_stock_candle(
        session=session, symbol=symbol, resolution=resolution
    )
    if not ohcl_json:
        return None
    df = pd.DataFrame(data=ohcl_json)
    df["timestamp"] = pd.to_datetime(df["date"]).dt.tz_localize("America/New_york")
    df["timestamp"] = df["timestamp"].dt.tz_convert("UTC")
    df["symbol"] = symbol
    return df[OHCL.names]


async def get_ohcl_data(
    session: aiohttp.ClientSession,
    start: Timestamp,
    end: Timestamp,
    symbols: List[str],
    frequency: str,
) -> pd.DataFrame:
    if start > end:
        raise ValueError("Start date cannot be greater than end date")
    if start.tz != pytz.UTC or end.tz != pytz.UTC:
        raise ValueError("Start and end dates must be UTC")

    print("Getting OHCL data")
    dfs = []
    for symbol in progress_bar(symbols):
        symbol_df = await get_ohcl_for_symbol(
            session=session, symbol=symbol, resolution=frequency
        )
        if symbol_df is not None:
            dfs.append(symbol_df)

    result_df = pd.concat(dfs)
    return result_df[(result_df.timestamp >= start) & (result_df.timestamp <= end)]


async def get_symbol_table(market: str) -> pa.Table:
    async with aiohttp.ClientSession() as session:
        symbol_df = await get_symbols(session=session, market=market)
        return pa.Table.from_pandas(symbol_df, schema=STOCK_SYMBOL)


async def get_ohcl_table_for(
    start: Timestamp, end: Timestamp, symbols: List[str], frequency: str
) -> pa.Table:
    async with aiohttp.ClientSession() as session:
        ohcl_df = await get_ohcl_data(
            session=session, start=start, end=end, symbols=symbols, frequency=frequency
        )
        return pa.Table.from_pandas(ohcl_df, schema=OHCL)


def pull_symbols(
    *, store: PriceStore, market: str, start: pd.Timestamp, end: pd.Timestamp
):
    symbol_table = asyncio.run(get_symbol_table(market=market))
    store.store_symbols(symbol_table=symbol_table, start=start, end=end, vendor="fmp")


def pull_ohcl_data(
    *,
    store: PriceStore,
    symbols: List[str],
    start: Timestamp,
    end: Timestamp,
    frequency: str,
):
    table = asyncio.run(get_ohcl_table_for(start, end, symbols, frequency))
    store.store_prices(
        price_table=table, start=start, end=end, vendor="fmp", frequency=frequency
    )


async def get_financials(
    symbols: List[str], start: pd.Timestamp, end: pd.Timestamp, statement, freq
) -> Optional[pa.Table]:
    """
    This endpoint gets all the available financials for a symbol,
    start and end are ignored but left for uniform interface across vendors
    Examples:
        table = await get_financials(["L.TO"], start, end, "bs", "quarterly") # Balance sheet pyarrow.Table
    """
    schema_map = {
        "bs": BALANCE_SHEET_V2,
        "ic": INCOME_STATEMENT_V2,
        "cf": CASHFLOW_STATEMENT_V2,
    }

    records = []
    async with aiohttp.ClientSession() as session:
        for symbol in progress_bar(symbols):
            result = await get_financials_for(session, symbol, statement, freq)
            if not result:
                logger.warn(f"Could not get {statement} financials for {symbol}")
                continue
            for record in result:
                records.append(record)

    if records:
        df = pd.DataFrame(data=records)
        df = normalize_names(df, statement)
        return pa.Table.from_pandas(df, schema=schema_map[statement])
    else:
        return None


def pull_financials(
    *, store, symbols, statements: Set[str], start: Timestamp, end: Timestamp
):
    type_to_statement = {
        "bs": "balance_sheet",
        "ic": "income_statement",
        "cf": "cashflow_statement",
    }

    if statements in set(type_to_statement.keys()):
        raise ValueError(
            f"statements:{statements} should be one of {type_to_statement.keys()}"
        )

    frequency = "quarter"
    for statement in statements:
        table = asyncio.run(get_financials(symbols, start, end, statement, frequency))
        store.store_financials(
            statement=type_to_statement[statement],
            financials_table=table,
            start=start,
            end=end,
            vendor="fmp",
        )
