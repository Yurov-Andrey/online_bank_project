import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize("card_number, correct_number", [('Счет 35383033474447895560', 'Счет **95560'),
                                                         ('Visa Classic 6831982476737658',
                                                          'Visa Classic 6831 98** **** 7658')])
def test_mask_account_card(card_number, correct_number):
    assert mask_account_card(
        card_number) == correct_number


def test_get_date(test_fixture_get_date_correct):
    assert get_date(test_fixture_get_date_correct) == '11.03.2024', '20.09.2024'


def test_get_date_missing_data(test_fixture_get_date_invalid_data):
    with pytest.raises(ValueError) as exc_info:
        get_date(test_fixture_get_date_invalid_data)

        assert str(exc_info.value) == "Данные о дате отсутствуют"
