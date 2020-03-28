# Regular Expression - substitution
import re
# re.sub(pattern,replacement,string)
a = '1212This is 1234 to 4567 haha'
#\d means digit
#\D means nonedigit
p = re.sub('\d.*','',a)
p = re.sub('\d','0',a)

a = 'This is 1234 to 4567 haha'
p = re.sub('\d.*','0',a)
p = re.sub('\D','0',a)
p = re.sub('\D.*','0',a)
# p = re.sub('\D.*','',a)
# p = re.sub('\D','',a)
print(p)