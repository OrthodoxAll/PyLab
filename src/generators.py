from typing import Any, Generator


def filter_by_currency(transactions: list[dict[str,Any]] ,currency: str) -> list[dict[str,Any]]:
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
    transactions_currency: Generator[dict[str, Any], Any, None] = (transaction for transaction in transactions
                                                                       if transaction["operationAmount"]["currency"]["code"] == currency)
    return transactions_currency

transactions = [{
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "USD",
                  "code": "RUB"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
      },
      {
              "id": 142264268,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "operationAmount": {
                  "amount": "79114.93",
                  "currency": {
                      "name": "USD",
                      "code": "USD"
                  }
              },
              "description": "Перевод со счета на счет",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
       },
      {
              "id": 142264268,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "operationAmount": {
                  "amount": "79114.93",
                  "currency": {
                      "name": "USD",
                      "code": "USD"
                  }
              },
              "description": "Перевод со счета на счет",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
       },
      {
              "id": 142264268,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "operationAmount": {
                  "amount": "79114.93",
                  "currency": {
                      "name": "USD",
                      "code": "RUB"
                  }
              },
              "description": "Перевод со счета на счет",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
       }]

usd_transactions = filter_by_currency(transactions, "RUB")
for _ in range(2):
    print(next(usd_transactions))


def transaction_descriptions(transactions: list[dict[str,Any]]) -> str:
    for transaction in transactions:
        yield transaction["description"]

description_transactions = transaction_descriptions(transactions)
for _ in range(4):
    print(next(description_transactions))


def card_number_generator(start:int, end:int)->str:
    """
    Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX.
    """
    # Итерируемся по диапазону от start до end (включительно)
    for number in range(start, end + 1):
        # Форматируем номер карты в строку длиной 16 символов,
        # заполняя ведущие нули до 16 цифр, если число меньше 10^16
        formatted_number = f'{number:016d}'
        # Создаем строку в формате XXXX XXXX XXXX XXXX
        # Используем срезы, чтобы разделить строку на части по 4 цифры
        yield f'{formatted_number[:4]} {formatted_number[4:8]} {formatted_number[8:12]} {formatted_number[12:]}'

for card_number in card_number_generator(1, 5):
    print(card_number)