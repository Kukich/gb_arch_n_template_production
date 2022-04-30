from framework.wsgi import WSGI,WSGI_DEBUG,WSGI_FAKE
from framework.conf import Conf

conf = Conf()
app = WSGI(conf)
#app = WSGI_DEBUG(conf)
#app = WSGI_FAKE(conf)


@app.route('^/contacts/?$','contacts.html')
def contacts(request):
    if(request.params.get('Гражданство',"") and request.params['Гражданство'] == 'НЕ РФ'):
        request.params['ne_rf_on'] = 'checked'
    else:
        request.params['rf_on'] = 'checked'
    request.params['name'] = 'contacts'
    return request.params