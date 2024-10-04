a=[1,4,7,9,10]
b=[1,2,3,6,7,12]
union=[]
inter=[]
for i in range(len(a)):
    if a[i] in b:
        inter.append(a[i])
        b.remove(a[i])
union=a+b


print(inter,union)