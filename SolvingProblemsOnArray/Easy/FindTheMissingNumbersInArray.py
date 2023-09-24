def find(arr,n):
    arr.sort()
    for i in range(0,n):
        if i != arr[i]:
            return i
        

if __name__ == "__main__":
    arr = [9,6,4,2,3,5,7,0,1]
    print(find(arr,len(arr)))