a=[1,4,-1,-7,5,-4,8,-10]
low,temp=0,0
for i in range(len(a)):
    if a[i]<0:
     temp=a[i]
     a[i]=a[low]
     a[low]=temp
     low+=1
print(a)