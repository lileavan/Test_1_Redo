import re
p=re.compile('([public|static|protected|private](/s))?[a-zA-Z_$0-9]*|([a-zA-Z_$]+[a-zA-Z_$0-9]*)')
print(p.match('public name'))
print(p.match('name'))
print(p.match('&&'))