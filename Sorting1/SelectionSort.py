n = 6
arr = [13,46,24,52,20,9]

for i in range(n-1):
    for j in range(i+1,n):
        if arr[i] > arr[j]:
            arr[i],arr[j] = arr[j],arr[i]
print(arr)