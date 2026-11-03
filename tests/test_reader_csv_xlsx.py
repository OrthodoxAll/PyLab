from unittest.mock import Mock, patch

import pandas as pd

from src.reader_csv_xlsx import read_transactions_csv, read_transactions_excel


@patch("src.reader_csv_xlsx.pd.read_csv")
def test_read_transactions_csv_returns_records(mock_read_csv):
    """Проверяет чтение CSV через pandas и преобразование в список словарей."""
    expected = [
        {
            "id": 650703,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210,
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        }
    ]

    mock_df = Mock()
    mock_df.to_dict.return_value = expected
    mock_read_csv.return_value = mock_df

    result = read_transactions_csv("transactions.csv")

    assert result == expected
    mock_read_csv.assert_called_once_with("transactions.csv", sep=";", encoding="utf-8")
    mock_df.to_dict.assert_called_once_with(orient="records")


def test_read_transactions_csv_from_file(tmp_path):
    """Проверяет чтение реального CSV-файла с разделителем «;»."""
    csv_path = tmp_path / "transactions.csv"
    csv_path.write_text(
        "id;state;date;amount;currency_name;currency_code;from;to;description\n"
        "650703;EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN;"
        "Счет 58803664561298323391;Счет 39745660563456619397;Перевод организации\n",
        encoding="utf-8",
    )
    result = read_transactions_csv(str(csv_path))
    assert result == [
        {
            "id": 650703,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210,
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        }
    ]

    def test_read_transactions_csv_without_rows_returns_empty_list(tmp_path):
        """Проверяет, что CSV только с заголовком возвращает пустой список."""
        csv_path = tmp_path / "empty.csv"
        csv_path.write_text(
            "id;state;date;amount;currency_name;currency_code;from;to;description\n",
            encoding="utf-8",
        )

        assert read_transactions_csv(str(csv_path)) == []


@patch("src.reader_csv_xlsx.pd.read_excel")
def test_read_transactions_excel_returns_records(mock_read_excel):
    """Проверяет чтение Excel через pandas и преобразование в список словарей."""
    expected = [
        {
            "id": 650703,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210,
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        }
    ]

    mock_df = Mock()
    mock_df.to_dict.return_value = expected
    mock_read_excel.return_value = mock_df

    result = read_transactions_excel("transactions.xlsx")

    assert result == expected
    mock_read_excel.assert_called_once_with("transactions.xlsx", engine="openpyxl")
    mock_df.to_dict.assert_called_once_with(orient="records")


def test_read_transactions_excel_from_file(tmp_path):
    """Проверяет чтение реального XLSX-файла через openpyxl."""
    excel_path = tmp_path / "transactions.xlsx"
    source = pd.DataFrame(
        [
            {
                "id": 650703,
                "state": "EXECUTED",
                "date": "2023-09-05T11:30:32Z",
                "amount": 16210,
                "currency_name": "Sol",
                "currency_code": "PEN",
                "from": "Счет 58803664561298323391",
                "to": "Счет 39745660563456619397",
                "description": "Перевод организации",
            }
        ]
    )
    source.to_excel(excel_path, index=False)

    result = read_transactions_excel(str(excel_path))

    assert result == [
        {
            "id": 650703,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210,
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        }
    ]


def test_read_transactions_excel_without_rows_returns_empty_list(tmp_path):
    """Проверяет, что Excel только с заголовком возвращает пустой список."""
    excel_path = tmp_path / "empty.xlsx"
    source = pd.DataFrame(
        columns=[
            "id",
            "state",
            "date",
            "amount",
            "currency_name",
            "currency_code",
            "from",
            "to",
            "description",
        ]
    )
    source.to_excel(excel_path, index=False)

    assert read_transactions_excel(str(excel_path)) == []
