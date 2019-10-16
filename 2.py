def sol(arr):
    for i in range(len(arr[0])):
        for j in range(1, len(arr)):
            if i==len(arr[j]) or arr[j-1][i]!=arr[j][i]:
                return i
    return len(arr[0])
	
print(sol(["apple", "apps", "ape"]))
print(sol(["hawaii", "happy"]))
print(sol(["dog", "dogs", "doge"]))