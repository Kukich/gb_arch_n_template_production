from framework.response import Response
from framework.request import Request
from jinja2 import Environment, FileSystemLoader
from framework.view import View
from framework.routes import Routes

class WSGI:
    def __init__(self,conf):
        self.conf = conf.config
        file_loader = FileSystemLoader(self.conf['main']['template_path'])
        env = Environment(loader=file_loader)
        self.template_env = env
        self.route_object= Routes(self.conf)

    def __call__(self, environ, start_response):
        """
        :param environ: словарь данных от сервера
        :param start_response: функция для ответа серверу
        """
        request = Request(environ)
        view = View(self.conf)
        contr_data = self.route_object.get_view_data(request)
        view_data = view(contr_data,request)
        html = self.render(contr_data["template"], data=view_data).encode()
        response = Response('200 OK',{'Content-Type': 'text/html'},html)
        # сначала в функцию start_response передаем код ответа и заголовки
        start_response(str(response.status_code), response.headers.items())
        # возвращаем тело ответа в виде списка из bite
        return [response.body]

    def route(self,url,template):
        def wrapper(func):
            self.route_object.routes.append({'path':url,'template':template,'func': func})
        return wrapper

    def render(self,template_name, **kwargs):
        """
        Минимальный пример работы с шаблонизатором
        :param template_name: имя шаблона
        :param kwargs: параметры для передачи в шаблон
        :return:
        """
        template = self.template_env.get_template(template_name)
        # Открываем шаблон по имени
        #with open(template_name, encoding='utf-8') as f:
            # Читаем
        #  template = Template(f.read())
        # рендерим шаблон с параметрами
        return template.render(**kwargs)

class WSGI_DEBUG(WSGI):
      def __call__(self,environ, start_response):
          request = Request(environ)
          print(request.env)
          print(request.params)
          return super().__call__(environ,start_response)


class WSGI_FAKE(WSGI):
    def __call__(self, environ, start_response):
        response = Response('200 OK', {'Content-Type': 'text/html'}, 'Hello from fake'.encode())
        start_response(str(response.status_code), response.headers.items())
        # возвращаем тело ответа в виде списка из bite
        return [response.body]