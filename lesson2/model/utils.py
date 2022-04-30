import yaml
import sys

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