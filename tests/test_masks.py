import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize("card_number", ['1596837868705199',
                                         '7158300734726758',
                                         '6831982476737658',
                                         '8990922113665229',
                                         '5999414228426353'])
def test_get_mask_card_number(card_number):
    assert get_mask_card_number


@pytest.mark.parametrize("account", ['64686473678894779589',
                                     '35383033474447895560',
                                     '73654108430135874305'])
def test_get_mask_account(account):
    assert get_mask_account


def test_get_mask_card_number_with_invalid_number():
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number('123456789012345')

        get_mask_card_number('')

    assert str(exc_info.value) == 'Не верная длина номера карты'


def test_get_mask_account_with_invalid_number():
    with pytest.raises(ValueError) as exc_info:
        get_mask_account('123456789')

        get_mask_account('')

    assert str(exc_info.value) == 'Не верная длина номера счета'


def test_get_mask_card_number_with_invalid_symbol():
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number('123номеркарты321')

    assert str(exc_info.value) == 'Номер карты должен состоять только из цифр'

def test_get_mask_account_with_invalid_symbol():
    with pytest.raises(ValueError) as exc_info:
        get_mask_account('00123номерсчета32100')

    assert str(exc_info.value) == 'Номер счета должен состоять только из цифр'