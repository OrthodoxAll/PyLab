import os

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

import pytest
from src.external_api import get_transaction_amount
from unittest.mock import patch
@pytest.mark.usefixtures("load_transactions_rub")
@pytest.mark.usefixtures("load_transactions_usd")

def test_get_transaction_amount_rub(load_transactions_rub):
    """
    проверяю когда рубли
    :return:
    """
    result = get_transaction_amount(load_transactions_rub)
    assert result == 49192.52

transaction_usd = {
    "operationAmount": {"amount": "10.0", "currency": {"code": "USD"}},
}

@patch("requests.get")
def test_get_transaction_amount_usd(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 1000}
    result = get_transaction_amount(transaction_usd)
    assert result == 1000
    # Проверяем правильность формирования url и headers
    amount = float(transaction_usd["operationAmount"]["amount"])
    currency = transaction_usd["operationAmount"]["currency"]["code"]
    expected_url = (
        f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
    )
    mock_get.assert_called_once_with(expected_url, headers={"apikey": API_KEY})

transaction_usd = {
    "operationAmount": {"amount": "200.0", "currency": {"code": "USD"}},
}

# Для проверки ошибки
@patch("requests.get")
def test_get_transaction_amount_api_error(mock_get):
    mock_get.return_value.status_code = 500
    mock_get.return_value.text = "Internal Server Error"
    with pytest.raises(ValueError, match="Failed to get currency rate"):
        get_transaction_amount(transaction_usd)

