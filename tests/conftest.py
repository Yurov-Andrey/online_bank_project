import pytest


@pytest.fixture
def test_fixture_correct_card():
    return '4235679800789899'


@pytest.fixture
def test_fixture_correct_account():
    return '35383033474447895560'


@pytest.fixture
def test_fixture_card_account_length_error():
    return '423567980078999'


@pytest.fixture
def test_fixture_card_digit_error():
    return '42356798ff898999'


@pytest.fixture
def test_fixture_account_digit_error():
    return '35383033a7444789556f'


@pytest.fixture
def test_fixture_correct_card_and_account():
    return [*'Счет 35383033474447895560',
            'Visa Classic 6831982476737658']


@pytest.fixture
def test_fixture_invalid_symbol_card():
    return [*'Visa Classic 6831982458', 'Visa ', '40817500']


@pytest.fixture
def test_fixture_invalid_symbol_account():
    return [*'Счет 3538303347', 'Счет ', '3568379579432385']


@pytest.fixture
def test_fixture_invalid_symbol_card_account():
    return ''


@pytest.fixture
def test_fixture_get_date_correct():
    return [*'2024-03-11T02:26:18.671407',
            '2024-09-20T09:40:30.399677']


@pytest.fixture
def test_fixture_get_date_invalid_data():
    return ''


@pytest.fixture
def test_fixture_filter_by_state_correct():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


@pytest.fixture
def test_fixture_filter_by_state_correct_canceled():
    return [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


@pytest.fixture
def test_fixture_filter_by_state_correct_executed():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]


@pytest.fixture
def test_fixture_sort_by_date():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


@pytest.fixture
def test_fixture_sort_by_date_correct():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
