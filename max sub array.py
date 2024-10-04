a=[1,4,7,3,-4,9,-6]
sum=a[0]
for i in range(1,len(a)-1):
    if a[i]>0:
        sum+=a[i]
    elif a[i]<0 and a[i+1]>-a[i]:
        sum+=a[i]
        print(sum)
