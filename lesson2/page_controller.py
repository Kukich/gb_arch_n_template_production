
def index(params):
    return {'name':'index','number_page': '1'}

def about(params):
    return {'name':'about','number_page': '2'}

def contacts(params):
    if(params.get('Гражданство',"") and params['Гражданство'] == 'НЕ РФ'):
        params['ne_rf_on'] = 'checked'
    else:
        params['rf_on'] = 'checked'
    params['name'] = 'contacts'
    if params.get('message', ''):
        print(params['message'])
    return params