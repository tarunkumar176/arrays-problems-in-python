a=[0,1,0,10,2,4]
n=len(a)
temp=0
for i in range((n-1),-1,-1):
    if a[i]==0:
        temp=a[i]
        a[i]=a[n-1]
        a[n-1]=temp
        n=n-1
print(a)