import finclaw.vendor.finnhub.models as mdls
from finclaw.data_store.schema import DIVIDEND


def test_to_dividend_table_conversion():
    symbol_dividend_records = [
        {
            "symbol": "AAPL",
            "date": "2019-05-10",  # ex-dividend date
            "amount": 0.77,
            "adjustedAmount": 0.77,
            "payDate": "2019-05-16",
            "recordDate": "2019-05-13",
            "declarationDate": "2019-05-01",
            "currency": "USD"
        },
    ]
    result = mdls.to_dividend_table(symbol_dividend_records)
    assert result.schema.names == DIVIDEND.names
