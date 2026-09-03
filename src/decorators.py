from datetime import datetime
import functools


def log(filename=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            def write_log(massage):
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(massage + "\n")
                else:
                    print(massage)

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


#########
