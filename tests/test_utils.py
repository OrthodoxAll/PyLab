import pytest
import json
from src.utils import load_transactions

# Тест: файл существует и содержит корректный список транзакций
def test_load_transactions_success(tmp_path):
    data = [
        {"id": 1, "amount": 100},
        {"id": 2, "amount": 200}
    ]
    file_path = tmp_path / "transactions.json"
    file_path.write_text(json.dumps(data), encoding="utf-8")
    result = load_transactions(str(file_path))
    assert result == data

# Тест: файл существует, но содержит не список (например, словарь)
def test_load_transactions_not_a_list(tmp_path):
    data = {"id": 1, "amount": 100}
    file_path = tmp_path / "transactions.json"
    file_path.write_text(json.dumps(data), encoding="utf-8")
    result = load_transactions(str(file_path))
    assert result == []

# Тест: файл не найден
def test_load_transactions_file_not_found():
    result = load_transactions("non_existent_file.json")
    assert result == []