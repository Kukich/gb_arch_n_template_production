import yaml
import time

def open_file(path):
    try:
        my_file = open(path, 'r')
    except FileNotFoundError:
        print("файла не существует ", path)
        return 0
    else:
        return my_file

def get_conf(name):
    stream = open_file(name)
    try:
        return yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)
        return 0
    finally:
        stream.close

def debug(func):
    def wrapper(*args, **kwargs):
        print(f'start {func.__name__}')
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time() - start_time
        print(f'{end_time} seconds')
        return res
    return wrapper