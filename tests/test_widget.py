import pytest

from src.widget import get_date, mask_account_card


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
