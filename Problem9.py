import re
p=re.compile('[+-]?(([0-9]*.[0-9]+)|([0-9]+.?))([eE][+-]?[0-9]+)?[lLfF]?')
print(p.match('0.0'))
print(p.match('0.'))
print(p.match('.0'))
print(p.match('0.0e-10f'))
print(p.match('0.0eE-10f'))