a=[1,5,4,3,8,6,10]
a.append(0)
n=len(a)
for i in range(n-1,-1,-1):
    a[i]=a[i-1]
del(a[n-1])
print(a)