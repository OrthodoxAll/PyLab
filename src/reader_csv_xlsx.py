import pandas as pd


def read_transactions_csv(path: str) -> list[dict]:
    """
    читает финансовые опреации из CSV
    :param path: путь к CSV
    :return: список словарей
    """
    data = pd.read_csv(path, sep=";", encoding="utf-8")
    return data.to_dict(orient="records")


def read_transactions_excel(path: str) -> list[dict]:
    """
    читает финансовые опреации из  Excel
    :param path: путь к Excel
    :return: список словарей
    """
    data = pd.read_excel(path, engine="openpyxl")
    return data.to_dict(orient="records")


if __name__ == "__main__":
    csv_read = read_transactions_csv("E:/Digital/bakend_programm/PythonProject/data/transactions.csv")
    print(csv_read)
    excel_read = read_transactions_excel("E:/Digital/bakend_programm/PythonProject/data/transactions_excel.xlsx")
    print(excel_read)
