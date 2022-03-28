
def index(request):
    return {'name':'index','number_page': '1'}

def about(request):
    return {'name':'about','number_page': '2'}

def contacts(request):
    if(request.params.get('Гражданство',"") and request.params['Гражданство'] == 'НЕ РФ'):
        request.params['ne_rf_on'] = 'checked'
    else:
        request.params['rf_on'] = 'checked'
    request.params['name'] = 'contacts'
    if request.params.get('message', ''):
        print(request.params['message'])
    return request.params