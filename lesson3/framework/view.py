import sys
import os
sys.path.append(os.path.join(os.getcwd(), '..'))
import page_controller

class View():
    def __call__(self,contr_data,request):
        output_function = {}
        try:
            output_function = getattr(page_controller, contr_data["controller"])
        except AttributeError as err:
            print(err)
            print(f"Need to create page_controller and include function {contr_data['controller']}")
        print(contr_data)
        return output_function(request)
