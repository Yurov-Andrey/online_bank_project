import shutil
from functools import wraps
from time import time


def log(filename=None):
    def wrapper(function):
        @wraps(function)
        def inner(*args, **kwargs):
            time_start = 0
            time_end = 0
            time_completed = time_end - time_start
            if filename is None:
                try:
                    time_start += time()
                    func_result = function(*args, **kwargs)
                    time_end += time()

                except Exception as e:
                    print(f'Function {function.__name__} started {time_start}')
                    print(f'{function.__name__} error: {e}. Inputs: {args}, {kwargs}')

                else:
                    print(f'{function.__name__} ok')
                    print(f'Function {function.__name__} started {time_start}')
                    print(f'Function {function.__name__} started {time_end}')
                    print(f'Time to complete the function {function.__name__} - {time_completed}')
                    return func_result

            elif filename is not None:
                try:
                    time_start += time()
                    func_result = function(*args, **kwargs)
                    time_end += time()

                except Exception as e:
                    logs_direct = './logs'
                    logs_direct_final = logs_direct + filename
                    with open(logs_direct_final, "a", encoding='utf-8') as file:
                        file.write(f'Function {function.__name__} started {time_start}\n')
                        file.write(f'{function.__name__} error: {e}. Inputs: {args}, {kwargs}\n')
                        # final_direct = './logs'
                        # shutil.move(filename, final_direct)

                else:
                    with open(filename, "a", encoding='utf-8') as file:
                        file.write(f'{function.__name__} ok \n')
                        file.write(f'Function {function.__name__} started {time_start}\n')
                        file.write(f'Function {function.__name__} started {time_end}\n')
                        file.write(f'Time to complete the function {function.__name__} - {time_completed}\n')
                        # final_direct = './logs'
                        # shutil.move(filename, final_direct)
                    return func_result

        return inner

    return wrapper


@log(filename="mylog.txt")
def my_function(x, y):
    return x + y


my_function(1, '2')
