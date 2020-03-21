# Bubble Sort
p = [9,5,8,4,6,2,7,1,3]
print("Before Sorting: ",p)
i = 0
while i < len(p):
    j = 0
    while j<i:
        if p[i]<p[j]:
            temp = p[i]
            p[i] = p[j]
            p[j] = temp
        j = j + 1
    i = i + 1
print("After Sorting: ",p)
