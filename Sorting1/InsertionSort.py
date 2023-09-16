n = 6
arr = [2,13,1,52,20,9]
# [2,13,1,52,20,9]

for i in range(n):
    k = i
    while(arr[k]<arr[k-1] and k != 0):
        arr[k],arr[k-1] = arr[k-1],arr[k]
        k -= 1
print(arr)
