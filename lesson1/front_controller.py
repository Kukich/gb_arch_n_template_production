import sys
import os
import yaml
import re
sys.path.append(os.path.join(os.getcwd(), '..'))
from model.utils import get_conf
import page_controller

def base_controller(environ):
    routes = get_conf('conf/routes.yaml')
    for route in routes:
        if(re.search(rf'{route["path"]}',environ["PATH_INFO"] )):
          output_function = getattr(page_controller, route["controller"])
          return {'template': route["template"],'data': output_function()}
    return {'template': 'index.html','data': {'name': 'default_index','number_page': '0'}}