from masks import get_mask_account, get_mask_card_number


def mask_account_card(type_number_card: str) -> str:
    """
    Маскирует карты и счета клиента
    :param type_number_card: Visa Platinum 7000792289606361
    или Счет 73654108430135874305  # входной аргумент
    :return: Visa Platinum 7000 79** **** 6361
    или Счет **4305 # выход функции
    """
    card_type = []  # создаем список для типа:карта, счет
    masked_number = ""  # создаем строку для хранения номера карты или счета
    parts = type_number_card.split()  # Разделяем входящую строку на части по пробелу
    for part in parts:  # проходимся по частям
        if part.isalpha():  # если часть это буквы то добавляем к списку типа
            card_type.append(part)
        else:  # в противном случае добавляем к строке номера
            masked_number += part
    card_type_str = " ".join(card_type)  # Соединяем слова списка в строку через пробел, на случай двойных названий
    if len(masked_number) == 16:  # проверем на соответсвие номеру карты
        maske = get_mask_card_number(masked_number)
    else:
        maske = get_mask_account(masked_number)

    return f"{card_type_str} {maske}"


str1 = "Счет 73654108430135874305"

print(mask_account_card(str1))


from datetime import datetime


def get_date(date_string: str) -> str:
    """
     Преобразует строку с датой в формате "YYYY-MM-DDTHH:MM:SS" в формат "ДД.ММ.ГГГГ".
    :param date_string:
    """
    try:
        dt = datetime.fromisoformat(date_string)  # Преобразуем строку в объект datetime
        return dt.strftime("%d.%m.%Y")  # Форматируем объект datetime в нужный формат
    except ValueError:
        return "Неверный формат даты"


str2 = "2024-03-11T02:26:18.671407"

print(get_date(str2))


# def get_date_iso(date_string: str) -> str:
#     date_part = date_string.split('T')[0] # Разделяем строку по "T" и берем только дату
#     year, month, day= date_part.split('-')
#     return f'{day}-{month}-{year}'
#
# print(get_date_iso(str2))
