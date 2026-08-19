import pytest


from src.masks import get_mask_card_number, get_mask_account

#from src.widget import mask_account_card

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


#def test_mask_account_card_valid(valid_mask_input_case):
   # for type_number_card, expected in valid_mask_input_case:
    # b    assert mask_account_card(type_number_card) == expected
