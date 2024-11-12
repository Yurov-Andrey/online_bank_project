import pytest


@pytest.fixture
def cards_numbers_and_accounts_for_test():
    return [('Maestro 1596837868705199',
             'Счет 64686473678894779589',
             'MasterCard 7158300734726758',
             'Счет 35383033474447895560',
             'Visa Classic 6831982476737658',
             'Visa Platinum 8990922113665229',
             'Visa Gold 5999414228426353',
             'Счет 73654108430135874305')]

@pytest.fixture
def date_test_text():
    return "2024-03-11T02:26:18.671407"

@pytest.fixture
def cards_numbers_test():
    return [('7158300734726758', '6831982476737658', '8990922113665229', '5999414228426353')]

@pytest.fixture
def accounts_for_test():
    return [('73654108430135874305', '35383033474447895560', '64686473678894779589')]