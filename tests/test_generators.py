import pytest

from src.generators import filter_by_currency, transaction_descriptions


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

def test_transaction_descriptions(transactions):
    #получаем виды операций
    des_transactions = transaction_descriptions(transactions)

    expected_des_transactions = [transactions[0]["description"],
                                transactions[1]["description"],
                                transactions[2]["description"],
                                transactions[3]["description"]
                                ]

    for expected in expected_des_transactions:
        assert next(des_transactions) == expected

    # Проверяем, что больше транзакций не осталось
    with pytest.raises(StopIteration):
        next(des_transactions)