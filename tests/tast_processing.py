import pytest

from src.processing import filter_by_state, sort_by_date


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
