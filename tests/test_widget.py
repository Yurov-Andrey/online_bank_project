import pytest

from src.widget import mask_account_card, get_date


def test_mask_account_card(test_fixture_correct_card_and_account):
    assert mask_account_card(
        test_fixture_correct_card_and_account) == 'Счет **95560', 'Visa Classic 6831 98** **** 7658'


def test_mask_account_card_length_account(test_fixture_invalid_symbol_account):
    with pytest.raises(ValueError) as exc_info:
        mask_account_card(test_fixture_invalid_symbol_account)

        assert str(exc_info.value) == "Не верная длина номера счета"


def test_mask_account_card_length_card(test_fixture_invalid_symbol_card):
    with pytest.raises(ValueError) as exc_info:
        mask_account_card(test_fixture_invalid_symbol_card)

        assert str(exc_info.value) == "Не верная длина номера карты"


def test_mask_account_card_missing_data(test_fixture_invalid_symbol_card_account):
    with pytest.raises(ValueError) as exc_info:
        mask_account_card(test_fixture_invalid_symbol_card_account)

        assert str(exc_info.value) == "Не верная длина номера карты"


def test_get_date(test_fixture_get_date_correct):
    assert get_date(test_fixture_get_date_correct) == '11.03.2024','20.09.2024'


def test_get_date_missing_data(test_fixture_get_date_invalid_data):
    with pytest.raises(ValueError) as exc_info:
        get_date(test_fixture_get_date_invalid_data)

        assert str(exc_info.value) == "Данные о дате отсутствуют"