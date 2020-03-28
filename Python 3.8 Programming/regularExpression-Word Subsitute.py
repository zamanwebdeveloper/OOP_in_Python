# word substitute
import re
a = 'This is a number 1234 5679'
# re.sub(pattern,replacement,string)
# \w = word charecter


# p = re.sub('\w+','$',a)
# p = re.sub('\w+s','$',a)
p = re.sub('\d+','$',a)
p = re.sub('\D+','$',a)
p = re.sub('\w+','zaman',a)
print(p)