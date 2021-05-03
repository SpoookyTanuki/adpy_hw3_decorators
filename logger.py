from datetime import datetime as dt
import hashlib
import os


def logger(output_file):
    def my_func(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(output_file, 'w', encoding='utf-8') as output:
                output.write(f'Function name: {func.__name__}\n'
                             f'Function execution date and time: {dt.now()}\n'
                             f'Our result is: {result}\n')
                if len(args) != 0:
                    output.write(f'Arguments are: {args}\n')
                if len(kwargs) != 0:
                    output.write(f'Arguments are: {kwargs}\n')
                print(f'Function name, date and time of execution, result, and args/kwargs '
                      f'(if exist) are in the file "{output_file}" now')
            return result
        return wrapper
    return my_func


@logger('output_file.txt')
def logger_testing():
    path = os.path.abspath('a_countries.txt')

    def hashing(line):
        yield hashlib.md5(line.encode()).hexdigest()
    with open(path) as file:
        for one_line in file:
            print(*hashing(one_line))


logger_testing()
# В файл записывается "Our result is: None", не знаю, в чём проблема и как *hashing можно записывать построчно
# В коде ниже всё норм работает

# @logger('output_file.txt')
# def adding_num(a, b):
#     result = a + b
#     return result
# adding_num(2, 5)
