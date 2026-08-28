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

