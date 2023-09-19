# def rotate(arr,n,r):
#     temp = []   #### Problem is here 
#     temp.extend(arr[n-r:])
#     temp.extend(arr[:n-r])
#     return temp

# if __name__  == "__main__":
#     arr = [1,2,3,4,5]
#     print(rotate(arr,len(arr),2))


# Most efficient code and brilliant method the Really admire the author of this code
def reverse(arr,start,end):
    while(start <= end):
        arr[start],arr[end] = arr[end],arr[start]
        start += 1
        end -= 1

if __name__  == "__main__":
    arr = [1,2,3,4,5]
    n = len(arr)
    r = 2
    reverse(arr,0,n-r-1)
    reverse(arr,n-r,n-1)
    reverse(arr,0,n-1)
    print(arr)