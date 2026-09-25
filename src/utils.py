import json
import logging
from os import name

logger = logging.getLogger('utils')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("../logs/utils.log", mode='w', encoding='utf-8')
file_handler.setLevel(logging.DEBUG)
file_formater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)


def load_transactions(path: str) -> list[dict]:
    """
    Читает данные о транзакциях'''

    :param path:  Путь до JSON-файла
    """
    try:
        logger.debug(f'Запгрузка транзакций из {path}')
        with open(path, "r", encoding="utf-8") as f:
            transactions = json.load(f)
            # print(f"Загруженные данные: {transactions}")  # Отладочная информация
            if isinstance(transactions, list):
                logger.debug(f"Успешно загружены транзакции из файла {path}")
                return transactions
            else:
                logger.error(f'Файл {path} не содержит транзапкций')
                return []
    except FileNotFoundError:
        logger.error(f"Файл не найден: {path}")
        print("Файл не найден")
        return []


print(load_transactions("../data/operations.json"))


########