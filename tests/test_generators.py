import pytest

from src.generators import filter_by_currency

def test_filter_by_currency(transactions):
    # Фильтруем по валюте USD
    usd_transactions = filter_by_currency(transactions, "USD")

    # Ожидаемые транзакции
    expected_transactions = [
        transactions[1],
        transactions[2]
    ]

    # Проверяем, что возвращаемые транзакции соответствуют ожидаемым
    for expected in expected_transactions:
        assert next(usd_transactions) == expected

    # Проверяем, что больше транзакций не осталось
    with pytest.raises(StopIteration):
        next(usd_transactions)