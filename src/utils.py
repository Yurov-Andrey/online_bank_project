import json
from typing import Any


def processing_json_dict(file_path: Any) -> list | str:
    """ Функция, которая принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список. """

    try:
        with (open(file_path, 'r', encoding='utf-8') as file):
            contents = json.load(file)

            if not isinstance(contents, list):
                empty_list = []
                return empty_list

            elif len(contents) == 0:
                empty_list = []
                return empty_list

            else:
                return contents

    except FileNotFoundError:
        return f"Запрашиваемый файл не найден или указан некорректный путь ({file_path}) к файлу"

    except json.JSONDecodeError:
        empty_list = []
        return empty_list
