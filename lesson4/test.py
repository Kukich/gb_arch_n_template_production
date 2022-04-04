import re
regular = '/education/(?P<lang>python|javascript|java)/(?P<level>high|middle|low)/?'
regular2 = '/education/(python|javascript|java)/(high|middle|low)/?'
string = '/education/python/high'
string2 = '/education/p/h'
params = {}
m = re.match(rf'{regular2}', string)
if(m):
    print(m.groupdict())
    print('ok')
    if (m.groupdict()):
        for k, v in m.groupdict().items():
            params[k] = v
print(params)