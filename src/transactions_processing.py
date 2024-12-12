import csv
import logging
import os
from typing import Any

import pandas as pd

log_dir = "../logs"
os.makedirs(log_dir, exist_ok=True)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(f"{log_dir}/transaction_processing.log", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(funcName)s - %(lineno)d: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def processing_csv(file_path: Any) -> list[dict] | str:
    """Функция для считывания финансовых операций из CSV принимает путь к файлу CSV в качестве аргумента и
    считывает финансовые операции из CSV, после чего выдает список словарей с транзакциями."""
    logger.info(f"Старт работы функции {processing_csv}, принят файл по пути {file_path}")
    try:

        if os.path.splitext(file_path)[1].lower() == ".csv":
            with open(file_path) as file:
                logger.info(f"Открыт и прочитан файл {file}")
                reader = csv.DictReader(file, delimiter=";")
                result = list(reader)

    except FileNotFoundError:
        logger.error(f"Запрашиваемый файл не найден или указан некорректный путь ({file_path}) к файлу")
        return f"Запрашиваемый файл не найден или указан некорректный путь ({file_path}) к файлу"

    except ValueError:
        logger.error("Файл по указанному пути не является csv файлом")
        return "Файл по указанному пути не является csv файлом"

    logger.info(f"Функция {processing_csv} завершила работу и вернула результат.")
    return result


def processing_excel():
    pass

# my_path_csv = '../data/transactions.csv'
# print(processing_csv(my_path_csv))
