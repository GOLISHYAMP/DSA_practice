n = 6
arr = [13,46,24,52,20,9]

for i in reversed(range(n-1)):
    for j in range(i):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
print(arr)