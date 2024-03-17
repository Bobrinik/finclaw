from finclaw.data_store.storage_clients.LocalStoreClient import LocalStoreClient
from finclaw.data_store.storeV2 import PriceStoreV2
from pathlib import Path

sc = LocalStoreClient()
price_store = PriceStoreV2("./data", sc, "fmp")
base_dir = "data/fmp/"


def test_get_symbol_store_path():
    result = price_store.get_ohclv_price_store_path("1")
    assert result == Path(base_dir + "ohclv/frequency_1")


def test_get_company_descriptions():
    result = price_store.get_company_descriptions()
    assert result == Path(base_dir + "company_descriptions")


def test_get_ownership_store_path():
    result = price_store.get_ownership_store_path("fund")
    assert result == Path(base_dir + "ownership/fund")


def test_get_insider_store_path():
    result = price_store.get_insider_store_path()
    assert result == Path(base_dir + "insider")


def test_get_dividend_store_path():
    result = price_store.get_dividend_store_path()
    assert result == Path(base_dir + "dividends")


def test_get_financial_statement_store_path():
    result = price_store.get_financial_statement_store_path("bs")
    assert result == Path(base_dir + "bs")


def test_get_split_store_path():
    result = price_store.get_split_store_path()
    assert result == Path(base_dir + "splits")
