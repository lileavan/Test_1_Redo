import re
p=re.compile('(?:/\\*(?;[^*]|(?:\\*+[^*/]))*\\*+/)|(?://.*)')
print(p.match('/*/* comment */'))
print(p.match('/*/* comment */ */'))
print(p.match('comment'))