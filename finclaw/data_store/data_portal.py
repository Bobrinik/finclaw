from collections import namedtuple
from datetime import timedelta
from typing import List, Optional, Union, Dict

import pandas as pd
import pyarrow as pa

from finclaw.config import settings
from finclaw.data_store.storeV2 import PriceStoreV2

DataChunk = namedtuple("DataChunk", ["current_date", "price_ohcl_daily"])


class Snapshot:
    def __init__(self, df: pd.DataFrame):
        self.data = df

    def history(self, days: int):
        """
        Get dataframe for the last n days
        :param days:
        :return:
        """
        return self.data[
            (self.data.index.max() - pd.Timedelta(days=days)) <= self.data.index
        ]


class DataPortal:
    """
    This is used by the simulation runner to answer questions about the data,
    like getting the prices of assets on a given day or to service history
    calls.
    """

    def __init__(
        self, price_store: PriceStoreV2, start: pd.Timestamp, end: pd.Timestamp, step
    ):
        self.price_data: Optional[pd.DataFrame] = None
        self._price_store = price_store
        self.current_date: pd.Timestamp = start
        self.start = start
        self.end = end
        self.step = step

    def load_price_data(
        self, *, start: pd.Timestamp, end: pd.Timestamp, frequency: str, vendor: str
    ) -> pa.Table:
        return self._price_store.load_prices(start=start, end=end, frequency=frequency)

    def init(self):
        price = self.load_price_data(
            start=self.start, end=self.end, frequency="D", vendor="finnhub"
        )
        df = price.to_pandas()
        df.index = df.timestamp
        self.price_data = df

    def get_simulation_data_frames(self):
        end = self.end
        while self.current_date < end:
            yield self.get_snapshot(current_date=self.current_date)
            self.current_date = self.current_date + timedelta(days=self.step)

    def get_snapshot(self, *, current_date: pd.Timestamp):
        if self.price_data is None:
            raise ValueError("You need to call initialize")

        # Note, we want a copy
        price_df = self.price_data[self.price_data.index <= current_date]

        return DataChunk(
            current_date=self.current_date, price_ohcl_daily=Snapshot(price_df)
        )


def list_vendors(
    storage_client, path=settings.TRADE_ENGINE_DATA, is_dict=False
) -> Union[List[PriceStoreV2], Dict[str, PriceStoreV2]]:
    if not is_dict:
        return [
            PriceStoreV2(path + "/" + ps_path, storage_client)
            for ps_path in storage_client.listdir(path)
        ]
    result = {}
    for ps_path in storage_client.listdir(path):
        ps = PriceStoreV2(path + "/" + ps_path, storage_client)
        result[f"{repr(ps)}"] = ps
    return result
