from src.processing import filter_by_state, sort_by_date
from tests.conftest import test_fixture_sort_by_date_correct, test_fixture_sort_by_date


def test_filter_by_state(test_fixture_filter_by_state_correct, test_fixture_filter_by_state_correct_executed):
    assert filter_by_state(test_fixture_filter_by_state_correct,
                           'EXECUTED') == test_fixture_filter_by_state_correct_executed


def test_filter_by_state_alt(test_fixture_filter_by_state_correct, test_fixture_filter_by_state_correct_canceled):
    assert filter_by_state(test_fixture_filter_by_state_correct,
                           'CANCELED') == test_fixture_filter_by_state_correct_canceled


def test_sort_by_date(test_fixture_sort_by_date, test_fixture_sort_by_date_correct):
    assert sort_by_date(test_fixture_sort_by_date) == test_fixture_sort_by_date_correct
