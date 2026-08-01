from typing import Union

PI = 3.14


def circle_area(r: Union[int, float]) -> Union[int, float]:
    """
    Расчет площади окроужности
    :param r: радиус
    :return: площадь
    """
    return PI * r ** 2


def format_description(r: Union[int, float], area: Union[int, float]) -> str:
    """
    Форматированный вывод информации об окружности
    :param r: радиуч
    :param area: площадь
    :return: информация об окружности
    """
    return f"Radius is   {r}  ; area is  {area:.2f}"


def get_info(r: Union[int, float]) -> None:
    """
    Получение информации об окружности
    :param r:
    """
    area = circle_area(r)
    description = format_description(r, area)
    print(description)


radius = int(input("Enter circle radius (int): "))
get_info(radius)
