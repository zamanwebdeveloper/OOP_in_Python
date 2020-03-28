# Regular Expression - match
import re
a = "My name is Syed Zaman and he is a student"
# re.match(pattern,string,flags(optional))
p = re.match('My.*',a)
p = re.match('name.*',a)
p = re.match('.*name.*',a)
p = re.match('(My.*)(and) (.*student)',a,re.I)

if p:
    print('match')
    print('Group-1: ',p.group(1))
    print('Group-2: ',p.group(2))
    print('Group-3: ',p.group(3))
else:
    print('Not match')