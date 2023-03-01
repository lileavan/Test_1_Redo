import re
p=re.compile('([0-9]|([1-9][0-9]*)|([0-7]+))|(0[xX][0-9a-fA-F]+(i64|I64|u|U|l|L)?')
print(p.match('0xABC192i64'))
