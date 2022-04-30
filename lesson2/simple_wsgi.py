import sys
import os
import yaml
from urllib.parse import unquote_plus,unquote
from jinja2 import Template
from model.utils import get_conf
from front_controller import base_controller

def application(environ, start_response):
    """
    :param environ: словарь данных от сервера
    :param start_response: функция для ответа серверу
    """
    main_configs = get_conf('conf/main.yaml')
    params = parse_data(environ)
    contr_data = base_controller(environ,params)
    html = render(os.path.join(main_configs["template_path"], contr_data["template"]),data=contr_data["data"])
    # сначала в функцию start_response передаем код ответа и заголовки
    start_response('200 OK', [('Content-Type', 'text/html')])
    # возвращаем тело ответа в виде списка из bite
    return [html.encode()]

def parse_data(env):
    method = env['REQUEST_METHOD']
    params = {}
    if(method == 'GET'):
        params = parse_get_data(env['QUERY_STRING'])
    else:
        # получаем длину тела
        content_length_data = env.get('CONTENT_LENGTH')
        # приводим к int
        content_length = int(content_length_data) if content_length_data else 0
        # считываем данные, если они есть
        params = parse_post_data(env['wsgi.input'].read(content_length)) if content_length > 0 else b''
    return params

def parse_get_data(data):
    result = {}
    if data:
       params = data.split('&')
       for p in params:
           k,v = p.split('=')
           result[unquote_plus(k)] = unquote_plus(v)
    return result

def parse_post_data(data):
    result = {}
    if data:
        # декодируем данные
        data_str = data.decode(encoding='utf-8')
        # собираем их в словарь
        result = parse_get_data(data_str)
    return result

def render(template_name, **kwargs):
    """
    Минимальный пример работы с шаблонизатором
    :param template_name: имя шаблона
    :param kwargs: параметры для передачи в шаблон
    :return:
    """

    # Открываем шаблон по имени
    with open(template_name, encoding='utf-8') as f:
        # Читаем
        template = Template(f.read())
    # рендерим шаблон с параметрами
    return template.render(**kwargs)

