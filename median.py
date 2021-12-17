def findMedian(arr):
    # Write your code here
    arr.sort()
    length=len(arr)
    mid=int(length/2)
    return(arr[mid])
  
arr=[]
n=int(input())
for i in range(0,n):
  element=int(input())
  arr.append(element)
  
findMedian(arr)
 
