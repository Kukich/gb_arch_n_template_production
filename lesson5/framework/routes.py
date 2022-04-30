import re

class Routes():
    def __init__(self,conf):
        self.routes = conf["routes"]

    def get_view_data(self,request):
        for route in self.routes:
            match = re.match(rf'{route["path"]}', request.env["PATH_INFO"])
            if (match):
                if(match.groupdict()):
                    for k,v in match.groupdict().items():
                        request.params[k] = v
                view_data ={}
                view_data["controller"] = route.get("controller","")
                view_data["func"] = route.get("func","")
                view_data["template"] = route["template"]
                return view_data
        return {'template': 'index.html', 'controller': 'index','func':''}