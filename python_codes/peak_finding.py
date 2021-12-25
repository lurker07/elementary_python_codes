arr=[10, 20, 15, 2, 23, 90, 67]
n=len(arr)
def peak(l,i):
    if(i+1<n and l[i]<l[i+1]):
        m=peak(l,i+1)
    elif(i-1>=0 and l[i]<l[i-1]):
        m=peak(l,i-1)
    else:
        m=l[i]
    return m
print(peak(arr,len(arr)//2))
