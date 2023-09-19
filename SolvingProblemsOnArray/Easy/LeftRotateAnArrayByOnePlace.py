def rotateArray(arr, n):
    t = arr[0]
    for i in range(1,n):
        arr[i-1] = arr[i]
    arr[n-1] = t
    return arr

arr = [5 ,7 ,3 ,2 ]
print(rotateArray(arr,len(arr)))