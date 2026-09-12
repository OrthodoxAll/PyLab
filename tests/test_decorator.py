import os
import re

import pytest

from src.decorators import log


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
