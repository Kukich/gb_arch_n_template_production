import sys
import os
import re
sys.path.append(os.path.join(os.getcwd(), '..'))
import page_controller

class View():
    def __init__(self,conf):
        self.conf = conf

    def __call__(self,contr_data,request):
        output_function = {}
        if(contr_data["func"] and callable(contr_data["func"])):
            output_function = contr_data["func"]
            return output_function(request)
        else:
            try:
               output_function = getattr(page_controller, contr_data["controller"])
            except AttributeError as err:
               print(err)
               print(f"Need to create page_controller and include function {contr_data['controller']}")
            return output_function(request)
