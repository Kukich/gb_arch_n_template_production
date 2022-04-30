from framework.utils import get_conf
import os

class Conf:
    def __init__(self,conf_path=os.path.join(os.getcwd(),'conf')):
        self.config = {}
        for conf_file in os.listdir(conf_path):
            if conf_file.endswith('.yaml'):
                self.config[conf_file[:-5]] = get_conf(os.path.join(conf_path,conf_file))




