# Dictionary and Comprehension
# a = {'apple':3}
# print(a['apple'])
# a = {1:1,2:4,3:9,4:16,5:25,.....}
a = {x:x**2 for x in range(1,6)}
a = {x:x**2 for x in range(1,21)if x%2 == 0}
a = {x**2:x for x in range(1,10)}
print(a)

