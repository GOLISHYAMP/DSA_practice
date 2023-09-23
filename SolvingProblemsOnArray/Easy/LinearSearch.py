def search(arr,n,num):
    for i in range(n):
        if arr[i] == num:
            return i
    return -1

if __name__ == "__main__":
    arr = [1, 2, 3, 2, 4, 5,]
    print(search(arr,len(arr),3))