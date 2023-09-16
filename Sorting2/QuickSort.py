def QuickSort(arr,low,high):
    if low < high:
        p_index = Partition(arr,low,high)
        QuickSort(arr,low,p_index-1)
        QuickSort(arr,p_index+1,high)

def Partition(arr,low,high):
    pivot = arr[low]
    i = low
    j = high
    while (i < j):
        while (arr[i] <= pivot and i <= high -1):
            i += 1
        while (arr[j] > pivot and j >= low+1):
            j -= 1
        if i < j:
            arr[i],arr[j] = arr[j],arr[i]
    arr[low],arr[j] = arr[j],arr[low]
    return j


if __name__ == "__main__":
    n = 6
    arr = [13,46,24,52,20,9]
    QuickSort(arr,0,n-1)
    print(arr)