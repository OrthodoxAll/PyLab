import pytest

from src.masks import get_mask_card_number, get_mask_account
from src.processing import filter_by_state, sort_by_date
from src.widget import mask_account_card, get_date


@pytest.mark.parametrize("card_number,expected", [
    ("7000792289606361", "7000 79** **** 6361"),
    ("1234567890123456", "1234 56** **** 3456"),
    ("5555666677778888", "5555 66** **** 8888"),
])


def test_get_mask_card_number(card_number,expected) :
    assert get_mask_card_number(card_number) == expected

def test_mask_card_number_valid(valid_card_numbers):
    for card_number, expected in valid_card_numbers:
        assert get_mask_card_number(card_number) == expected

def test_mask_card_number_invalid(invalid_card_numbers):
    for card_number in invalid_card_numbers:
        with pytest.raises(ValueError):
            get_mask_card_number(card_number)


@pytest.mark.parametrize ('account_number,expected',
                          [("73654108430135874305", "**4305"),
                            ("12345678901234567890", "**7890"),
                            ("98765432109876543210", "**3210"),
                            ])

def test_get_mask_account(account_number, expected):
    assert get_mask_account(account_number) == expected


@pytest.mark.parametrize ('account_number',
                          [("1"),
                           ("1111111111111111111111111111111111111"),
                           ("123456789123456789AS"),
                           ("7365-4108-4301-3587-4305"),
                           ("123456789O1234567890"),# буква 'O' среди цифр
])

def test_get_mask_account_invalid(account_number):
    with pytest.raises(ValueError):
        get_mask_account(account_number)

# Модуль widget


def test_mask_account_card_valid(valid_mask_input_case):
   for type_number_card, expected in valid_mask_input_case:
       assert mask_account_card(type_number_card) == expected

def test_mask_account_card_invalid(invalid_mask_input_case):
    for type_number_card in invalid_mask_input_case:
        with pytest.raises(AttributeError):
            assert mask_account_card(type_number_card)


def test_get_date_valid(valid_date):
    for date_string, expected in valid_date:
        assert get_date(date_string) == expected

def test_get_date_invalid(invalid_date):
    for date_string in invalid_date:
        with pytest.raises(TypeError):
            assert get_date(date_string)


# Млдуль processing
def test_filter_by_state_empty():
    assert filter_by_state([], "EXECUTED") == []
    assert filter_by_state([], "ANY_STATUS") == []


@pytest.mark.parametrize ("state,expected_ids", [
    ("EXECUTED", [1, 4]),           # стандартный статус
    ("PENDING", [2]),               # другой статус
    ("FAILED", [3]),                # еще один статус
    ("CANCELLED", []),])             # статус отсутствует


def test_filter_by_state(sample_data, state, expected_ids):
    filtered = filter_by_state(sample_data, state)
    result_ids = [item['id'] for item in filtered]
    assert result_ids == expected_ids

# Проверка работы по умолчанию (state='EXECUTED')
def test_filter_by_state_default(sample_data):
    filtered = filter_by_state(sample_data)
    result_ids = [item['id'] for item in filtered]
    assert result_ids == [1, 4]


def test_sort_by_date_empty(): # на пустую дату
    assert sort_by_date([]) == []


@pytest.mark.parametrize ("date", [
    ( {'id': 20, 'date': 'notadate'}),
    ({'id': 21, 'date': '2022/01/01 14:30:00'}),
    ({'id': 22, 'date': None}),
    ({'id': 23}),])


def test_sort_by_date( date):
    with pytest.raises(AttributeError):
        assert sort_by_date(date)



def test_sort_by_date_equal_dates():
    data = [
        {'id': 10, 'date': '2020-01-01T12:00:00'},
        {'id': 11, 'date': '2020-01-01T12:00:00'},
        {'id': 12, 'date': '2020-01-01T12:00:00'},
    ]
    result = sort_by_date(data)
    result_ids = [item['id'] for item in result]
    assert set(result_ids) == {10, 11, 12}  # порядок любой, главное — все на месте