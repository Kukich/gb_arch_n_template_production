from education import EducationFabric

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

def education(request):
    langs = ['python','java','javascript']
    menu = []
    for l in langs:
        obj = EducationFabric(l).object
        mlist = obj.menu_headers()
        for m in mlist:
            menu.append(m)
    return {'menu_educations':menu}

def education_page(request):

    menu_dict = education(request)
    print(menu_dict)
    obj_education = EducationFabric(request.params["lang"])
    education_object = obj_education.create_level_page(request.params["level"])
    print(education_object)
    return {'menu_educations': menu_dict["menu_educations"],'education': education_object}