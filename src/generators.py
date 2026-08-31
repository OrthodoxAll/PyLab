from typing import Any, Generator


def filter_by_currency(transactions: list[dict[str, Any]], currency: str) -> Generator[dict[str, Any], None, None]:
    """
    Функция возвращает итератор, который выдает транзакции с заданной валютой.
    :param transactions:
    :param currency: "USD"
    :return:{
           "id": 939719570,
           "state": "EXECUTED",
           "date": "2018-06-30T02:08:58.425572",
           "operationAmount": {
               "amount": "9824.07",
               "currency": {
                   "name": "USD",
                   "code": "USD"
               }
           },
           "description": "Перевод организации",
           "from": "Счет 75106830613657916952",
           "to": "Счет 11776614605963066702"
     }
    """
    transactions_currency: Generator[dict[str, Any], Any, None] = (
        transaction for transaction in transactions if transaction["operationAmount"]["currency"]["code"] == currency
    )
    return transactions_currency


def transaction_descriptions(transactions: list[dict[str, Any]]) -> Generator[dict[str, Any], Any, None]:
    """
    принимает список словарей с транзакциями и возвращает описание каждой операции по очереди.
    """
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, end: int) -> Generator[str, None, None]:
    """
    Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX.
    """
    # Итерируемся по диапазону от start до end (включительно)
    for number in range(start, end + 1):
        # Форматируем номер карты в строку длиной 16 символов,
        # заполняя ведущие нули до 16 цифр, если число меньше 10^16
        formatted_number = f"{number:016d}"
        # Создаем строку в формате XXXX XXXX XXXX XXXX
        # Используем срезы, чтобы разделить строку на части по 4 цифры
        yield f"{formatted_number[:4]} {formatted_number[4:8]} {formatted_number[8:12]} {formatted_number[12:]}"
