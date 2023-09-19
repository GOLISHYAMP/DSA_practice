def is_sorted(arr):
    for i in range(len(arr)-2):
        if arr[i] > arr[i+1]:
            return False
    return True
            
if __name__ == "__main__":
    arr = [6,5,4,3,2,1]
    print(is_sorted(arr))