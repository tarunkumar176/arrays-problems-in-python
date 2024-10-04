a=[1,5,4,-7,8,2,10]
max,min=a[0],a[0]
for i in range(len(a)):
    if a[i]>max:
        max=a[i]
    if a[i]<min:
        min=a[i]
print(min,max)