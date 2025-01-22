import csv
import logging
import os
from typing import Any

import pandas as pd

from src.settings import REPORTS_PATH

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(f"{REPORTS_PATH}/transaction_processing.log", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(funcName)s - %(lineno)d: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def processing_csv(file_path: Any) -> list[dict] | str:
    """Функция для считывания финансовых операций из CSV. Принимает путь к файлу CSV в качестве аргумента и
    считывает финансовые операции из CSV, после чего выдает список словарей с транзакциями."""

    logger.info(f"Старт работы функции {processing_csv}, принят файл по пути {file_path}")
    result = []

    if os.path.splitext(file_path)[1].lower() != ".csv":
        return "Файл по указанному пути не является csv файлом"

    try:
        with open(file_path, mode="r", encoding="utf-8") as file:
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


def processing_excel(file_path: Any) -> list[dict] | str:
    """Функция для считывания финансовых операций из xlsx. Принимает путь к файлу xlsx в качестве аргумента и
    считывает финансовые операции из xlsx, после чего выдает список словарей с транзакциями."""

    logger.info(f"Старт работы функции {processing_excel}, принят файл по пути {file_path}")

    if os.path.splitext(file_path)[1].lower() != ".xlsx":
        return "Файл по указанному пути не является xlsx файлом"

    try:
        xlsx = pd.read_excel(file_path)
        result_list_excel = xlsx.to_dict(orient="records")
        logger.info(f"Функция {processing_excel} завершила работу и вернула результат.")
        return result_list_excel

    except FileNotFoundError:
        logger.error(f"Запрашиваемый файл не найден или указан некорректный путь ({file_path}) к файлу")
        return f"Запрашиваемый файл не найден или указан некорректный путь ({file_path}) к файлу"

    except ValueError:
        logger.error("Файл по указанному пути не является xlsx файлом")
        return "Файл по указанному пути не является xlsx файлом"
