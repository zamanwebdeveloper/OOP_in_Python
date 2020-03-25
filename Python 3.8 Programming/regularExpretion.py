# Regular Expression
import re # r = regular and e = expression

a = "My name is Zaman and i am a python programmer"
# re.search(pattern,string,flags<optional>)
# (.*---.*)
# . means match any character * means zero or more
# flags <optional>
# re.I means case insensitive
p = re.search('.*And.*',a,re.I)
p = re.search('.*is.*',a,re.I)
p = re.search('.*iss.*',a,re.I)
if p:
    print('Found')
else:
    print('Not Found')

