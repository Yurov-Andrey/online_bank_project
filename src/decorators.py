import os
from functools import wraps
import time


def log(filename=None):
    """Декоратор, который автоматически логирует начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки. Декоратор может логировать работу функции и ее результат как в файл,
     так и в консоль"""

    def wrapper(function):
        @wraps(function)
        def inner(*args, **kwargs):
            time_start = 0
            time_end = 0

            if filename is None:
                try:
                    time_start += time.time()
                    func_result = function(*args, **kwargs)
                    time_end += time.time()

                except Exception as e:
                    print(f"{function.__name__} error: {e}. Inputs: {args}, {kwargs}")

                    return "ValueError"

                else:
                    time_completed = round(time_end - time_start, 5)
                    print(
                        f"{function.__name__} ok\nFunction {function.__name__} started {time_start}\n"
                        f"Function {function.__name__} started {time_end}\n"
                        f"Time to complete the function: {function.__name__} - {time_completed}"
                    )

                return func_result

            elif filename is not None:
                log_dir = "logs"
                os.makedirs(log_dir, exist_ok=True)
                log_path = os.path.join(log_dir, filename)

                try:
                    time_start += time.time()
                    func_result = function(*args, **kwargs)
                    time_end += time.time()

                except Exception as e:
                    with open(log_path, "a", encoding="utf-8") as file:
                        file.write(f"{function.__name__} error: {e}. Inputs: {args}, {kwargs}\n")

                    return "ValueError"

                else:
                    time_completed = round(time_end - time_start, 5)
                    with open(log_path, "a", encoding="utf-8") as file:
                        file.write(f"{function.__name__} ok \n")
                        file.write(f"Function {function.__name__} started {time_start}\n")
                        file.write(f"Function {function.__name__} started {time_end}\n")
                        file.write(f"Time to complete the function: {function.__name__} - {time_completed}\n")

                return func_result

        return inner

    return wrapper
