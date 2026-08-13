from typing import Any


def filter_by_state(data: list[dict[str, Any]], state: str = "EXECUTED") -> list[dict[str, Any]]:
    """
        принимает список словарей и опционально значение для ключа
    state
     (по умолчанию
    'EXECUTED'
    ). Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
    state
     соответствует указанному значению.
        :param data: [{'id': 414288290, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
     {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
        :param state: 'EXECUTED'
    """

    return [item for item in data if item.get("state") == state]


def sort_by_date(data: list[dict[str, Any]], descending: bool = True) -> list[dict[str, Any]]:
    """
    принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание).
    Функция должна возвращать новый список, отсортированный по дате
    (date).
    :param data: [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]
    :param descending: True по умолчанию убывание , от свежей даты к старшей
    """
    data_filtered = filter(lambda item: item.get("date") is not None, data)
    return list(sorted(data_filtered, key=lambda x: x["date"], reverse=descending))  # сортировка data
