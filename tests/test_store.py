import pytz

from finclaw.data_store.store import PriceStore
from finclaw.data_store.schema import OHCL, STOCK_SYMBOL
import pandas as pd
import pyarrow as pa

# TODO:
# Do the same for news store
# [] Add test for saving price data from dataframe use OHCL schema
# [] Add test for savign symbol data from dataframe use symbol schema
# [] Add test for loading symbols
# [] Add test for loading price

symbol = pa.array(["AAPL"])
timestamp = pa.array([pd.Timestamp("2020-01-01 12:00:00", unit="s", tz=pytz.UTC)])
open = pa.array([1])
high = pa.array([12])
close = pa.array([11])
low = pa.array([1])
volume = pa.array([100])

PRICE_TABLE = pa.Table.from_arrays(
    [symbol, timestamp, open, high, close, low, volume], schema=OHCL
)

START = pd.Timestamp("2020-01-01", unit="s", tz=pytz.UTC).normalize()
END = pd.Timestamp("2021-01-01", unit="s", tz=pytz.UTC).normalize()

ticker = pa.array(["AAPL"])
figi = pa.array(["BBG000B9Y5X2"])
type = pa.array(["Common Share"])
mic = pa.array(["XNGS"])
description = pa.array(["APPLE INC"])
currency_name = pa.array(["USD"])

SYMBOL_TABLE = pa.Table.from_arrays(
    [ticker, figi, type, mic, description, currency_name], schema=STOCK_SYMBOL
)


def test_save_and_load(tmp_path):
    folder = tmp_path / ""
    store = PriceStore(str(folder))
    store.store(
        symbol_table=SYMBOL_TABLE,
        price_table=PRICE_TABLE,
        start=START,
        end=END,
        frequency="D",
        vendor="test",
    )
    price_table = store.load_prices(start=START, end=END, frequency="D")
    symbol_table = store.load_symbols(start=START, end=END, vendor="test")

    assert price_table.schema == PRICE_TABLE.schema
    assert price_table == PRICE_TABLE

    assert symbol_table.schema == SYMBOL_TABLE.schema
    assert symbol_table == SYMBOL_TABLE
