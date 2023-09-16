def InsertionSort(arr,i,n):
    if i>=n:
        return
    k = i
    while(arr[k]<arr[k-1] and k != 0):
        arr[k],arr[k-1] = arr[k-1],arr[k]
        k -= 1
    InsertionSort(arr,i+1,n)

if __name__ == "__main__":
    n = 6
    arr = [13,46,24,52,20,9]
    InsertionSort(arr,0,n)
    print(arr)