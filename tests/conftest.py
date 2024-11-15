import pytest


@pytest.fixture
def test_fixture_mask_account_card():
    return [*'Счет 35383033474447895560',
            'Visa Classic 6831982476737658']


@pytest.fixture
def test_fixture_get_date():
    return [*"2024-03-11T02:26:18.671407",
            "2024-09-20T09:40:30.399677"]


@pytest.fixture
def test_fixture_mask_account_card_with_invalid_symbol():
    return [*'']


@pytest.fixture
def test_fixture_get_date_invalid_data():
    return [*"222222222222222222222", "yuyuyuyuy",
            "..........", "", "2024"]
