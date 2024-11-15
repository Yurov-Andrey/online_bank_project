import pytest

from tests.conftest import test_fixture_get_date, test_fixture_mask_account_card
from src.widget import mask_account_card, get_date


def test_mask_account_card_correct(test_fixture_mask_account_card):
    assert mask_account_card(test_fixture_mask_account_card) == 'Счет **9556', 'Visa Classic 6831 98** **** 7658'


def test_get_date(test_fixture_get_date):
    assert get_date(test_fixture_get_date) == '11.03.2024', '20.09.2024'


def test_mask_account_card_value_error_1():
    with pytest.raises(ValueError) as exc_info:
        mask_account_card('Visa')

    assert str(exc_info.value) == 'Отсутствует номер счета или карты'


def test_mask_account_card_value_error_2():
    with pytest.raises(ValueError) as exc_info:
        mask_account_card('Visa 1431234')

    assert str(exc_info.value) == 'Не верная длина номера карты'


def test_mask_account_card_value_error_3():
    with pytest.raises(ValueError) as exc_info:
        mask_account_card('Счет 40817810')

    assert str(exc_info.value) == 'Не верная длина номера счета'
