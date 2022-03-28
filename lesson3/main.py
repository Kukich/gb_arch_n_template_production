from framework.wsgi import WSGI
from framework.conf import Conf

conf = Conf()
app = WSGI(conf)