from education import EducationFabric
from framework.utils import debug

@debug
def index(request):
    return {'name':'index','number_page': '1'}

def about(request):
    return {'name':'about','number_page': '2'}

def education(request):
    langs = ['python','java','javascript']
    menu = []
    for l in langs:
        obj = EducationFabric(l).object
        mlist = obj.menu_headers()
        for m in mlist:
            menu.append(m)
    return {'menu_educations':menu}

@debug
def education_page(request):
    menu_dict = education(request)
    obj_education = EducationFabric(request.params["lang"])
    education_object = obj_education.create_level_page(request.params["level"])
    return {'menu_educations': menu_dict["menu_educations"],'education': education_object}