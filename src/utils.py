import json


def load_transactions(path: str) -> list[dict]:
    """
    Читает данные о транзакциях'''

    :param path:  Путь до JSON-файла
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            transactions = json.load(f)
            # print(f"Загруженные данные: {transactions}")  # Отладочная информация
            if isinstance(transactions, list):
                return transactions
            else:
                return []
    except FileNotFoundError:
        print("Файл не найден")
        return []

print(load_transactions('../data/operations.json'))
