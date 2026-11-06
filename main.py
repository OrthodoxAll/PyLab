from pathlib import Path
from typing import Any

from src.processing import filter_by_state, process_bank_search, sort_by_date
from src.reader_csv_xlsx import read_transactions_csv, read_transactions_excel
from src.utils import load_transactions
from src.widget import get_date, mask_account_card

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
STATUSES = ("EXECUTED", "CANCELED", "PENDING")

def get_amount_and_currency(transaction: dict[str, Any]) -> tuple[float, str]:
    """
    Возвращает сумму и код валюты для JSON, CSV и XLSX.

    :param transaction: словарь с транзакцией
    :return: сумма и код валюты
    """
    operation_amount = transaction.get("operationAmount")

    if isinstance(operation_amount, dict):
        amount = operation_amount.get("amount", 0)
        currency = operation_amount.get("currency", {}).get("code", "")
    else:
        amount = transaction.get("amount", 0)
        currency = transaction.get("currency_code", "")

    return float(amount), str(currency)


def filter_rub_transactions(data: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """
    Оставляет только рублёвые операции.

    :param data: список словарей с транзакциями
    :return: список транзакций в рублях
    """
    return [
        transaction
        for transaction in data
        if get_amount_and_currency(transaction)[1] == "RUB"
    ]


def format_amount(amount: float, currency: str) -> str:
    """
    Форматирует сумму для вывода.

    :param amount: сумма операции
    :param currency: код валюты
    :return: строка вида «Сумма: 40542 руб.»
    """
    if amount.is_integer():
        value = str(int(amount))
    else:
        value = f"{amount:.2f}".rstrip("0").rstrip(".")

    suffix = "руб." if currency == "RUB" else currency
    return f"Сумма: {value} {suffix}"


def print_transaction(transaction: dict[str, Any]) -> None:
    """
    Печатает одну банковскую операцию.

    :param transaction: словарь с транзакцией
    """
    date = get_date(str(transaction.get("date", "")))
    description = transaction.get("description", "")

    print(f"{date} {description}")

    from_account = transaction.get("from")
    to_account = transaction.get("to")

    if from_account and to_account:
        print(
            f"{mask_account_card(str(from_account))} -> "
            f"{mask_account_card(str(to_account))}"
        )
    elif to_account:
        print(mask_account_card(str(to_account)))

    amount, currency = get_amount_and_currency(transaction)
    print(format_amount(amount, currency))
    print()


def load_data(choice: str) -> tuple[list[dict[str, Any]], str]:
    """
    Загружает транзакции из выбранного источника.

    :param choice: пункт меню: 1 — JSON, 2 — CSV, 3 — XLSX
    :return: список транзакций и название формата
    """
    if choice == "1":
        return load_transactions(str(DATA_DIR / "operations.json")), "JSON"

    if choice == "2":
        return read_transactions_csv(str(DATA_DIR / "transactions.csv")), "CSV"

    return read_transactions_excel(str(DATA_DIR / "transactions_excel.xlsx")), "XLSX"


def ask_yes_no(question: str) -> bool:
    """
    Задаёт вопрос с ответом «Да» или «Нет».

    :param question: текст вопроса
    :return: True для «Да», False для «Нет»
    """
    while True:
        answer = input(question).strip().lower()

        if answer in {"да", "yes", "y", "д"}:
            return True

        if answer in {"нет", "no", "n", "н"}:
            return False

        print("Пожалуйста, введите «Да» или «Нет».")


def choose_status() -> str:
    """
    Запрашивает корректный статус операции.

    :return: статус в верхнем регистре
    """
    print("Введите статус, по которому необходимо выполнить фильтрацию.")
    print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")

    while True:
        user_input = input().strip()
        status = user_input.upper()

        if status in STATUSES:
            print(f'Операции отфильтрованы по статусу "{status}"')
            return status

        print(f'Статус операции "{user_input}" недоступен.')
        print("Введите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")


def main() -> None:
    """Основная логика работы программы с пользователем."""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    while True:
        choice = input().strip()
        if choice in {"1", "2", "3"}:
            break
        print("Введите 1, 2 или 3.")

    transactions, source = load_data(choice)
    print(f"Для обработки выбран {source}-файл.")

    status = choose_status()
    transactions = filter_by_state(transactions, status)

    if ask_yes_no("Отсортировать операции по дате? Да/Нет\n"):
        direction = input(
            "Отсортировать по возрастанию или по убыванию?\n"
        ).strip().lower()

        while direction not in {"по возрастанию", "по убыванию"}:
            print("Введите «по возрастанию» или «по убыванию».")
            direction = input(
                "Отсортировать по возрастанию или по убыванию?\n"
            ).strip().lower()

        transactions = sort_by_date(
            transactions,
            descending=direction == "по убыванию",
        )

    if ask_yes_no("Выводить только рублевые транзакции? Да/Нет\n"):
        transactions = filter_rub_transactions(transactions)

    if ask_yes_no(
        "Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n"
    ):
        search = input("Введите слово для поиска: ").strip()
        transactions = process_bank_search(transactions, search)

    print("Распечатываю итоговый список транзакций...")

    if not transactions:
        print(
            "Не найдено ни одной транзакции, подходящей под ваши "
            "условия фильтрации"
        )
        return

    print(f"Всего банковских операций в выборке: {len(transactions)}")
    print()

    for transaction in transactions:
        print_transaction(transaction)


if __name__ == "__main__":
    main()