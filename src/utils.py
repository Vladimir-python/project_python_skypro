﻿import json
import logging

import pandas as pd
from src.decorators import log


""" создаем логгер для логирования функций и пишем логи в директорию logs"""
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s:%(name)s - %(levelname)s - %(message)s",
    filename="C:/PythonProjects/python_skypro_new_project/project_skypro_new/logs/utils.log",  # Запись логов в файл
    filemode="w",
)  # Перезапись файла при каждом запуске
logger = logging.getLogger("utils.py")


#@log("logs/work_func.txt")
def get_info_transactions(path_file: str) -> list[dict]:
    """
    Функция принимает путь до файла и возвращает операции в исходном файле
    в формате list[dict]
    """
    try:
        logger.info("Открываем файл...")

        with open(path_file, encoding="utf-8") as file:
            try:
                file_dict = json.load(file)
                logger.info("смотрим содержимое файла, ждем формат list()")

                if type(file_dict) is not list:
                    logger.warning("файл не формата list()")
                    return []

                logger.info("файл корректный, возвращаем содержимое")
                return file_dict

            except json.JSONDecodeError:
                logger.warning("файл не может быть прочитан, неверный формат")
                return []

    except FileNotFoundError:
        logger.warning("файл не найден, неверный путь до файла")
        return []


# @log("logs/work_func.txt")
def get_info_transactions_csv(path_file: str) -> list[dict] | list:
    """
    Функция принимает путь до файла и возвращает операции в исходном файле
    в формате list[dict]
    """
    try:
        logger.info("Открываем файл...")

        with open(path_file, encoding="utf-8") as file:
            try:
                file_dict = pd.read_csv(file, delimiter=";")
                logger.info("смотрим содержимое файла, ждем формат pd.DataFrame")

                if type(file_dict) is not pd.DataFrame:
                    logger.warning("файл не формата pd.DataFrame")
                    return []

                logger.info("файл корректный, возвращаем содержимое")
                return file_dict.to_dict(orient="records")
            except json.JSONDecodeError:
                logger.warning("файл не может быть прочитан, неверный формат")
                return []

    except FileNotFoundError:
        logger.warning("файл не найден, неверный путь до файла")
        return []


# @log("logs/work_func.txt")
def get_info_transactions_xlsx(path_file: str) -> list[dict] | list:
    """
    Функция принимает путь до файла и возвращает операции в исходном файле
    в формате list[dict]
    """
    try:
        logger.info("Открываем файл...")

        file_dict = pd.read_excel(path_file, index_col=0)
        logger.info("смотрим содержимое файла, ждем формат pd.DataFrame")

        if type(file_dict) is not pd.DataFrame:
            logger.warning("файл не формата pd.DataFrame")
            return []

        logger.info("файл корректный, возвращаем содержимое")
        return file_dict.to_dict(orient="records")
    except json.JSONDecodeError:
        logger.warning("файл не может быть прочитан, неверный формат")
        return []

    except FileNotFoundError:
        logger.warning("файл не найден, неверный путь до файла")
        return []
