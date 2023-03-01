import re
p=re.compile('([^.]+.[#!%$‘&+*–/=?^_`{|}~0-9a-zA-Z]+)|[#!%$‘&+*–/=?^_`{|}~0-9a-zA-Z]+')
print(p.match('firstpart'))
print(p.match('..--.'))
print(p.match('firstpart.lastpart.'))
print(p.match('firstpart.lastpart'))