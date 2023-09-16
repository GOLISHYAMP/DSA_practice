def mergeSort(arr,low,high):
    if low >= high:
        return
    mid = int((high+low)/2)
    mergeSort(arr,low,mid)
    mergeSort(arr,mid+1,high)
    merge(arr,low,mid,high)

def merge(arr,low,mid,high):
    # global a
    temp = []
    left = low
    right = mid+1
    while (left <= mid and right <= high):
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
    
    while (left <= mid):
        temp.append(arr[left])
        left += 1
    
    while (right <= high):
        temp.append(arr[right])
        right += 1

    # for i in range(len(temp)):
    #     a[i] = temp[i]
    # print(temp)
    for i in range(low, high + 1):
        arr[i] = temp[i - low]

if __name__ == "__main__":
    n = 6
    a = [13,46,24,52,20,9]
    mergeSort(a,0,n-1)
    # merge(a,0,int((n-1)/2),n-1)
    print(a)
