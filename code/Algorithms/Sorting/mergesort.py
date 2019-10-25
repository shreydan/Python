def merge(arr,l,mid,r):
    L=[0]*(mid-l+1)
    R=[0]*(r-mid)
    for i in range(0,mid-l+1):
        L[i]=arr[l+i]
    for i in range(0,r-mid):
        R[i]=arr[mid+1+i]
    i=j=0
    k=l
    while i!=len(L) and j!=len(R):
        if L[i]<=R[j]:
            arr[k]=L[i]
            i+=1
        else:
            arr[k]=R[j]
            j+=1
        k+=1
    while i<len(L):
        arr[k]=L[i]
        k+=1
        i+=1
    while j<len(R):
        arr[k]=R[j]
        k+=1
        j+=1
def mergeSort(arr,l,r):
    cnt=0
    if l<r:
        mid=(l+r)//2
        mergeSort(arr,l,mid)
        mergeSort(arr,mid+1,r)
        merge(arr,l,mid,r)