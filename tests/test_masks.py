import pytest

from src.masks import get_mask_account, get_mask_card_number
from tests.conftest import test_fixture_correct_card


def test_get_mask_card_number(test_fixture_correct_card):
    assert get_mask_card_number(test_fixture_correct_card) == '4235 67** **** 9899'


def test_get_mask_account(test_fixture_correct_account):
    assert get_mask_account(test_fixture_correct_account) == '**95560'


@pytest.mark.parametrize("card_number, correct_number", [
    ('1596837868705199', '1596 83** **** 5199'),
    ('7158300734726758', '7158 30** **** 6758')
])
def test_get_mask_card_number_2(card_number, correct_number):
    assert get_mask_card_number(card_number) == correct_number


@pytest.mark.parametrize("account_number, correct_number", [
    ('12347656709834567890', '**67890'),
    ('12649005678789000863', '**00863')
])
def test_get_mask_account_2(account_number, correct_number):
    assert get_mask_account(account_number) == correct_number


def test_get_mask_card_length(test_fixture_card_account_length_error):
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(test_fixture_card_account_length_error)

    assert str(exc_info.value) == "Не верная длина номера карты"


def test_get_mask_account_length(test_fixture_card_account_length_error):
    with pytest.raises(ValueError) as exc_info:
        get_mask_account(test_fixture_card_account_length_error)

    assert str(exc_info.value) == "Не верная длина номера счета"


def test_get_mask_account_digits(test_fixture_account_digit_error):
    with pytest.raises(ValueError) as exc_info:
        get_mask_account(test_fixture_account_digit_error)

    assert str(exc_info.value) == "Номер счета должен состоять только из цифр"


def test_get_mask_card_digits(test_fixture_card_digit_error):
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(test_fixture_card_digit_error)

    assert str(exc_info.value) == "Номер карты должен состоять только из цифр"
