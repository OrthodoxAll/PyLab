def filter_by_state(data: list[dict], state: str = 'EXECUTED') -> list[dict]:
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
    # filtered_items=[] # создаем пустой список
    # for item in data: # проходим по словаряь
    #     if item.get('state') == state: # проверяем совпадение со state
    #         filtered_items.append(item)
    # return filtered_items
    return [item for item in data if item.get('state') == state]

print(filter_by_state([{'id': 414288290, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
 {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
 {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}],'CANCELED'))


def sort_by_date(data: list[dict], descending:bool =True) -> list[dict]:
    """
    принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание).
    Функция должна возвращать новый список, отсортированный по дате
    (date).
    :param data: [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]
    :param descending: True по умолчанию убывание , от свежей даты к старшей
    """
    return sorted(data, key= lambda x: x.get('date'), reverse=descending)

print(sort_by_date([{'id': 414288290, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
 {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
 {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}], False))