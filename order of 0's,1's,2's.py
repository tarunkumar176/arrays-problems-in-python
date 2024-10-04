a=[0,2,1,0,1,2,2]
low,temp,high=0,0,len(a)-1
for i in range(len(a)):
    if a[i]==0:
        temp=a[i]
        a[i]=a[low]
        a[low]=temp
        low+=1
temp=0
for i in range(len(a)-1,-1,-1):
    if a[i]==2:
        temp=a[i]
        a[i]=a[high]
        a[high]=temp
        high-=1
print(a)
        