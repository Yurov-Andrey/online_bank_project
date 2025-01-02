from unittest.mock import mock_open, patch

import pandas as pd

from src.transactions_processing import processing_csv, processing_excel


@patch(
    "builtins.open",
    new_callable=mock_open,
    read_data=("id;state;date;amount;currency_name;currency_code;from;to;description\n"
"650703;EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN;Счет 58803664561298323391;Счет 39745660563456619397;Перевод организации\n"
"3598919;EXECUTED;2020-12-06T23:00:58Z;29740;Peso;COP;Discover 3172601889670065;Discover 0720428384694643;Перевод с карты на карту\n"
"593027;CANCELED;2023-07-22T05:02:01Z;30368;Shilling;TZS;Visa 1959232722494097;Visa 6804119550473710;Перевод с карты на карту\n"
"5380041;CANCELED;2021-02-01T11:54:58Z;23789;Peso;UYU;;Счет 23294994494356835683;Открытие вклада\n")
)
def test_processing_csv(mock_file, test_transaction_csv_imitation):
    result = processing_csv("data/transactions.csv")

    assert result == test_transaction_csv_imitation
    mock_file.assert_called_once_with("data/transactions.csv", mode="r", encoding="utf-8")


@patch("builtins.open", side_effect=FileNotFoundError)
def test_processing_csv_file_not_found(mock_file):
    result = processing_csv("data/non_existent_file.csv")
    expected_result = "Запрашиваемый файл не найден или указан некорректный путь (data/non_existent_file.csv) к файлу"

    assert result == expected_result
    mock_file.assert_called_once_with("data/non_existent_file.csv", mode="r", encoding="utf-8")


@patch("builtins.open", side_effect=ValueError)
def test_processing_csv_not_csv(mock_file):
    result = processing_csv("data/transactions.txt")
    expected_result = "Файл по указанному пути не является csv файлом"

    assert result == expected_result
    mock_file.assert_not_called()


@patch("pandas.read_excel")
def test_processing_excel_correct(mock_read_excel, test_transaction_excel_imitation):
    mock_read_excel.return_value = pd.DataFrame(test_transaction_excel_imitation)

    result = processing_excel("data/transactions.xlsx")

    assert result == test_transaction_excel_imitation
    mock_read_excel.assert_called_once_with("data/transactions.xlsx")


@patch("pandas.read_excel", side_effect=FileNotFoundError)
def test_processing_excel_file_not_found(mock_read_excel):
    result = processing_excel("data/transactions.xlsx")

    assert result == "Запрашиваемый файл не найден или указан некорректный путь (data/transactions.xlsx) к файлу"
    mock_read_excel.assert_called_once_with("data/transactions.xlsx")


@patch("pandas.read_excel", side_effect=ValueError)
def test_processing_excel_not_xlsx(mock_read_excel):
    result = processing_excel("data/transactions.txt")

    assert result == "Файл по указанному пути не является xlsx файлом"
    mock_read_excel.assert_not_called()


