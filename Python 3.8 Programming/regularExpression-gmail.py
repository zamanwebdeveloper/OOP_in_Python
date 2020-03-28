# searching - g mail
import re
a = 'zaman.mbs@gmail.com'
a = 'zaman.mbs@hotmail.com'
a = 'zaman.mbs@hotmail.in'
#re.search(pattern,string,flags<optional>)
# \W = Word Character
# + = one or more . = amu character
# * = zero or more
p = re.search('\w+\.+\w+@gmail.com',a)
p = re.search('\w+\.*\w+@\w+.com',a)
p = re.search('\w+\.*\w+@\w+\.\w+',a)

if p:
    print('Found')
else:
    print("Not Found")