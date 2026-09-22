import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")


def get_transaction_amount(transaction: dict) -> float:
    """Получение суммы транзакции в рублях."""
    amount = float(transaction["operationAmount"]["amount"])  # Получаем сумму транзакции
    currency = transaction["operationAmount"]["currency"]["code"]  # Получаем валюту
    if currency == "RUB":
        return amount  # Если уже в рублях, просто возвращаем сумму
    else:
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=" f"{currency}&amount={amount}"
        headers = {"apikey": API_KEY}
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            raise ValueError(f"Failed to get currency rate {response.text}")
        return round(response.json()["result"], 2)


transaction = {
    "id": 172864002,
    "state": "EXECUTED",
    "date": "2018-12-28T23:10:35.459698",
    "operationAmount": {"amount": "49192.52", "currency": {"name": "USD", "code": "USD"}},
}

print(get_transaction_amount(transaction))
