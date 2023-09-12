n = 6
arr = [2,13,1,52,20,9]
# [2,13,1,52,20,9]

for i in range(1,n):
    k = i-1
    # print("Value of k: ",k)
    while (arr[k] > arr[k+1]) and k>=0:
        arr[k],arr[k+1] = arr[k+1],arr[k]
        k -= 1
    print(arr)
print(arr)