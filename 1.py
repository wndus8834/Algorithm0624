def quick_sorted(arr):
   if len(arr) > 1:
       pivot = arr[len(arr)-1]
       left, mid, right = [], [], []
       for i in range(len(arr)-1):
           if arr[i] > pivot:
               left.append(arr[i])
           elif arr[i] < pivot:
               right.append(arr[i])
           else:
               mid.append(arr[i])
       mid.append(pivot)
       return quick_sorted(left) + mid + quick_sorted(right)
   else:
       return arr

def NMAX(arr,b):
    if(len(arr)>=b):
        arr=quick_sorted(arr)
        print(arr[b-1])
    else:
        print("err")

NMAX([-1,3,-1,5,4],2)
NMAX([2,4,-2,-3,8],1)
NMAX([-5,-3,1],3)