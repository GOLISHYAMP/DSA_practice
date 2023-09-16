def BubbleSort(arr,n):
    if n == 0:
        return
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            arr[i],arr[i+1] = arr[i+1],arr[i]
    
    BubbleSort(arr,n-1)

if __name__ == "__main__":
    n = 6
    arr = [13,46,24,52,20,9]
    BubbleSort(arr,n)
    print(arr)