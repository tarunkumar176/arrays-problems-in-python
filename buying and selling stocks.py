'''a=[100,180,260,310,40,535,695]'''
a=[4,2,2,2,4]
n=len(a)
max1=0
for i in range(1,n):
    if a[i]>a[i-1]:
        max1+=a[i]-a[i-1]
print(max1)