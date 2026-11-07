import pytest

from src.processing import filter_by_state, sort_by_date, process_bank_operations, process_bank_search


def test_filter_by_state_empty():
    assert filter_by_state([], "EXECUTED") == []
    assert filter_by_state([], "ANY_STATUS") == []


@pytest.mark.parametrize(
    "state,expected_ids",
    [
        ("EXECUTED", [1, 4]),  # стандартный статус
        ("PENDING", [2]),  # другой статус
        ("FAILED", [3]),  # еще один статус
        ("CANCELLED", []),
    ],
)  # статус отсутствует
def test_filter_by_state(sample_data, state, expected_ids):
    filtered = filter_by_state(sample_data, state)
    result_ids = [item["id"] for item in filtered]
    assert result_ids == expected_ids


# Проверка работы по умолчанию (state='EXECUTED')
def test_filter_by_state_default(sample_data):
    filtered = filter_by_state(sample_data)
    result_ids = [item["id"] for item in filtered]
    assert result_ids == [1, 4]


def test_sort_by_date_empty():  # на пустую дату
    assert sort_by_date([]) == []


@pytest.mark.parametrize(
    "date",
    [
        ({"id": 20, "date": "notadate"}),
        ({"id": 21, "date": "2022/01/01 14:30:00"}),
        ({"id": 22, "date": None}),
        ({"id": 23}),
    ],
)
def test_sort_by_date(date):
    with pytest.raises(AttributeError):
        assert sort_by_date(date)


def test_sort_by_date_equal_dates():
    data = [
        {"id": 10, "date": "2020-01-01T12:00:00"},
        {"id": 11, "date": "2020-01-01T12:00:00"},
        {"id": 12, "date": "2020-01-01T12:00:00"},
    ]
    result = sort_by_date(data)
    result_ids = [item["id"] for item in result]
    assert set(result_ids) == {10, 11, 12}  # порядок любой, главное — все на месте


def test_process_bank_search_is_case_insensitive():
    data = [
        {"description": "Перевод организации"},
        {"description": "Перевод с карты на карту"},
    ]

    assert process_bank_search(data, "перевод организации") == [data[0]]


def test_process_bank_search_finds_substring():
    data = [{"description": "Перевод организации"}]

    assert process_bank_search(data, "организации") == data


def test_process_bank_search_returns_empty_list_without_matches():
    data = [{"description": "Перевод организации"}]

    assert process_bank_search(data, "оплата") == []


def test_process_bank_search_skips_transactions_without_description():
    data = [{"id": 1}, {"description": "Перевод организации"}]

    assert process_bank_search(data, "перевод") == [data[1]]


def test_process_bank_search_returns_empty_list_for_empty_search():
    data = [{"description": "Перевод организации"}]

    assert process_bank_search(data, "") == []


def test_process_bank_search_handles_special_characters():
    data = [{"description": "Перевод 100% суммы"}]

    assert process_bank_search(data, "100%") == data


def test_process_bank_operations_counts_categories():
    data = [
        {"description": "Перевод организации"},
        {"description": "Перевод организации"},
        {"description": "Перевод с карты на карту"},
        {"description": "Оплата услуг"},
    ]
    categories = ["Перевод организации", "Перевод с карты на карту"]

    assert process_bank_operations(data, categories) == {
        "Перевод организации": 2,
        "Перевод с карты на карту": 1,
    }


def test_process_bank_operations_ignores_unknown_categories():
    data = [{"description": "Оплата услуг"}]

    assert process_bank_operations(data, ["Перевод организации"]) == {}


def test_process_bank_operations_returns_empty_dict_for_empty_data():
    assert process_bank_operations([], ["Перевод организации"]) == {}


def test_process_bank_operations_returns_empty_dict_for_empty_categories():
    data = [{"description": "Перевод организации"}]

    assert process_bank_operations(data, []) == {}
