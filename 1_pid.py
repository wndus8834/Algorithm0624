def nMax(arr,b):
    if(len(arr)>=b):
        arr.sort(reverse=True)
        print(arr[b-1])
    else:
        print("err")

nMax([-1,3,-1,5,4],2)
nMax([2,4,-2,-3,8],1)
nMax([-5,-3,1],3)