import pytest


from src.masks import get_mask_card_number, get_mask_account

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