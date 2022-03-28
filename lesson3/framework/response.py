
class Response:
    def __init__(self,status_code=200,headers: dict=None,body: str = ''):
        self.status_code = status_code
        self.headers = headers
        self.body = body
