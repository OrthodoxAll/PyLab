import pytest


from src.widget import mask_account_card
from src.masks import get_mask_account, get_mask_card_number

def test_mask_account_card_valid(valid_mask_input_case):
   for type_number_card, expected in valid_mask_input_case:
       assert mask_account_card(type_number_card) == expected