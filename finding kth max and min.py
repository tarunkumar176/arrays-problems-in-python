a=[18,10,5,9,11,6]
k=3
count1,count2,kmin,kmax=0,0,0,0
for i in range(len(a)):
    for j in range(len(a)):
        if a[i]>a[j]:
            count1+=1
        if a[i]<a[j]:
            count2+=1
    if count1==k-1:
        kmin=a[i]
    else:
        count1=0
    if count2==k-1:
        kmax=a[i]
    else:
        count2=0
print(kmin,kmax)