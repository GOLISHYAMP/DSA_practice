n = 6
arr = [13,2,1,52,20,9]
[2,13,1,52,20,9]

for i in range(1,n):
    k = i-1
    while arr[k] > arr[]:
        arr[k],arr[j] = arr[j],arr[k]
        k -= 1
    