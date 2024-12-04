import json
import os
from unittest.mock import patch, mock_open

from src.utils import processing_json_dict


def test_processing_json_dict(test_fixture_processing_json_dict_correct_list):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    my_json = os.path.join(base_dir, 'data', 'operations.json')
    assert processing_json_dict(my_json) == test_fixture_processing_json_dict_correct_list


@patch("builtins.open", new_callable=mock_open)
def test_processing_json_dict_correct_file(mock_file, test_fixture_processing_json_dict_correct_list):
    mock_file.return_value.read.return_value = json.dumps(test_fixture_processing_json_dict_correct_list)
    result = processing_json_dict("mocked_path.json")
    assert result == test_fixture_processing_json_dict_correct_list
    mock_file.assert_called_once_with("mocked_path.json", "r", encoding="utf-8")


@patch("builtins.open", new_callable=mock_open, read_data='')
def test_processing_json_dict_empty_file(mock_file):
    result = processing_json_dict("mocked_path.json")
    assert result == []
    mock_file.assert_called_once_with("mocked_path.json", "r", encoding="utf-8")


@patch("builtins.open", new_callable=mock_open, read_data='{"key": value}')
def test_processing_json_dict_invalid_json(mock_file):
    result = processing_json_dict("mocked_path.json")
    assert result == []
    mock_file.assert_called_once_with("mocked_path.json", "r", encoding="utf-8")


@patch("builtins.open", side_effect=FileNotFoundError)
def test_processing_json_dict_file_not_found(mock_file):
    result = processing_json_dict("nonexistent_file.json")
    assert result == "Запрашиваемый файл не найден или указан некорректный путь (nonexistent_file.json) к файлу"
    mock_file.assert_called_once_with("nonexistent_file.json", "r", encoding="utf-8")
