from urllib.parse import unquote_plus,unquote

class Request:
    def __init__(self,env):
        self.params = self.parse_data(env)
        self.env = env
        self.headers = {}
        for key,value in env.items():
            if(key.startswith('HTTP')):
                self.headers[key[:5]]=value

    def parse_data(self, env):
        method = env['REQUEST_METHOD']
        params = {}
        if (method == 'GET'):
            params = self.parse_get_data(env['QUERY_STRING'])
        else:
            # получаем длину тела
            content_length_data = env.get('CONTENT_LENGTH')
            # приводим к int
            content_length = int(content_length_data) if content_length_data else 0
            # считываем данные, если они есть
            params = self.parse_post_data(env['wsgi.input'].read(content_length)) if content_length > 0 else b''
        return params


    def parse_get_data(self, data):
        result = {}
        if data:
            params = data.split('&')
            for p in params:
                k, v = p.split('=')
                result[unquote_plus(k)] = unquote_plus(v)
        return result


    def parse_post_data(self, data):
        result = {}
        if data:
            # декодируем данные
            data_str = data.decode(encoding='utf-8')
            # собираем их в словарь
            result = self.parse_get_data(data_str)
        return result