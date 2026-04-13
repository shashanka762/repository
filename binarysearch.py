# program to demonstrate binary search
def binarysearch(array,low,high,key):
    low=o,high=len(array)-1
  
    mid=int(len(array)/2)
    while(low<=high): 
        if(key==mid):
            return mid
        else if(key>mid);
            low=mid+1
        else:
            high=mid-1
array=(13,24,35,46,57,68,29)
key=45
pos=binarysearch(array,low,high,key)
if(pos==-1):
    print("element is not found")
else:
    print("element is found at=",pos)        