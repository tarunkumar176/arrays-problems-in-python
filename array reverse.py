a=[1,5,4,-7,8,2,10]
'''print(a[::-1])direct method'''
low=0
high=len(a)-1
temp=0
while(low<high):
    temp=a[low]
    a[low]=a[high]
    a[high]=temp
    low=low+1
    high=high-1
print(a)