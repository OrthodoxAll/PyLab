import pytest

from src.generators import (
    card_number_generator,
    filter_by_currency,
    transaction_descriptions,
)


def test_filter_by_currency(transactions):
    # Фильтруем по валюте USD
    usd_transactions = filter_by_currency(transactions, "USD")

    # Ожидаемые транзакции
    expected_transactions = [transactions[1], transactions[2]]

    # Проверяем, что возвращаемые транзакции соответствуют ожидаемым
    for expected in expected_transactions:
        assert next(usd_transactions) == expected

    # Проверяем, что больше транзакций не осталось
    with pytest.raises(StopIteration):
        next(usd_transactions)


def test_transaction_descriptions(transactions):
    # получаем виды операций
    des_transactions = transaction_descriptions(transactions)

    expected_des_transactions = [
        transactions[0]["description"],
        transactions[1]["description"],
        transactions[2]["description"],
        transactions[3]["description"],
    ]

    for expected in expected_des_transactions:
        assert next(des_transactions) == expected

    # Проверяем, что больше транзакций не осталось
    with pytest.raises(StopIteration):
        next(des_transactions)


def test_card_number_generator():
    # Проверка работы генератора для диапазона от 1 до 15
    expected = [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005",
        "0000 0000 0000 0006",
        "0000 0000 0000 0007",
        "0000 0000 0000 0008",
        "0000 0000 0000 0009",
        "0000 0000 0000 0010",
        "0000 0000 0000 0011",
        "0000 0000 0000 0012",
        "0000 0000 0000 0013",
        "0000 0000 0000 0014",
        "0000 0000 0000 0015",
    ]
    generated = list(card_number_generator(1, 15))
    assert generated == expected

    # Проверка работы генератора для диапазона с одним элементом (10 до 10)
    expected = ["0000 0000 0000 0010"]
    generated = list(card_number_generator(10, 10))
    assert generated == expected

    # Проверка работы генератора для диапазона от 9999 до 10000
    expected = ["0000 0000 0000 9999", "0000 0000 0001 0000"]

    generated = list(card_number_generator(9999, 10000))
    assert generated == expected
