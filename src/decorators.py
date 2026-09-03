import functools
from datetime import datetime
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    Автоматически логирует начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки.
    :param filename: (str, optional) Имя файла для сохранения лога.
    Если не указано — вывод в консоль.
    :return: декоратор
    """

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        """
        Декоратор-обёртка для заданной функции. Добавляет логирование при каждом вызове.

        :param func: функция, которую требуется логировать
        :return: обёрнутая функция
        """

        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            """
            Внутренняя обёртка. Выполняет логирование до и после вызова функции,
                       а также при возникновении исключений.
            """

            def write_log(massage):
                """
                Записывает строку лога в файл или выводит в консоль, в зависимости от настроек.
                """
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(massage + "\n")
                else:
                    print(massage)

            start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # определяем время начала
            try:
                result = func(*args, **kwargs)
                end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                # определяем время завершения
                write_log(f"{func.__name__} ok " f"Время начала - {start_time}. Время окончания - {end_time} ")
                return result
            except Exception as e:
                end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                write_log(
                    f"{func.__name__} error: {str(e)}. Inputs: {args}, {kwargs} "
                    f"Время начала - {start_time}. Время окончания - {end_time}"
                )
                raise

        return wrapper

    return decorator


#########
