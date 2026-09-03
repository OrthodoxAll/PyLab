import os
import re
from datetime import datetime
import pytest
import functools


def log(filename=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            def write_log(message):
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(message + "\n")
                else:
                    print(message)

            start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            try:
                result = func(*args, **kwargs)
                end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
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


# @pytest.fixture(autouse=True)
# def cleanup_logfile():
#     logfile = "test_log.txt"
#     if os.path.exists(logfile):
#         os.remove(logfile)
#     yield
#     if os.path.exists(logfile):
#         os.remove(logfile)


def test_success_file():
    logfile = "test_log.txt"

    @log(filename=logfile)
    def plus(a, b):
        return a + b

    plus(2, 3)
    with open(logfile, encoding="utf-8") as f:
        text = f.read()
    assert "plus ok" in text
    assert "Время начала - " in text
    assert "Время окончания - " in text
    assert re.search(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}", text)


def test_error_file():
    logfile = "test_log.txt"

    @log(filename=logfile)
    def div(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        div(1, 0)
    with open(logfile, encoding="utf-8") as f:
        text = f.read()
    assert "div error:" in text
    assert "Inputs: (1, 0), {}" in text
    assert re.search(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}", text)


def test_success_file_mul():
    logfile = "test_log.txt"

    @log(filename=logfile)
    def mul(a, b):
        return a * b

    mul(4, 5)
    with open(logfile, encoding="utf-8") as f:
        text = f.read()
    assert "mul ok" in text
    assert "Время начала - " in text
    assert "Время окончания - " in text
    assert re.search(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}", text)


def test_error_file_sub():
    logfile = "test_log.txt"

    @log(filename=logfile)
    def sub(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        sub(10, 0)
    with open(logfile, encoding="utf-8") as f:
        text = f.read()
    assert "sub error:" in text
    assert "Inputs: (10, 0), {}" in text
    assert re.search(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}", text)


# Очистка test_log.txt после всех тестов
@pytest.fixture(scope="session", autouse=True)
def cleanup_logfile():
    yield  # Тесты выполняются после yield
    logfile = "test_log.txt"
    if os.path.exists(logfile):
        os.remove(logfile)


##############
