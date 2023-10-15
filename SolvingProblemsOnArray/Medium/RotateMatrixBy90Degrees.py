# Brute force method

# def rotateMatrix(mat,n):
#     temp = []
#     for i in range(n):
#         temp.append([0]*n)
#     cnt = n-1
#     for i in range(n):
#         for j in range(n):
#             temp[j][cnt] = mat[i][j]
#         cnt -= 1
#     return temp

# Optimized method in this method first we will transpose the matrix and 
# each of the rows in the matrix

def rotateArrayInplace(arr,n):
    left = 0
    right = n-1
    while(left < right):
        arr[left],arr[right] = arr[right],arr[left]
        left += 1
        right -= 1
    return arr


def rotateMatrix(mat,n):
    for i in range(n):
        for j in range(i,n):
            mat[i][j],mat[j][i] = mat[j][i],mat[i][j]

    for i in range(n):
        mat[i] = rotateArrayInplace(mat[i],n)
    
    return mat

if __name__ == "__main__":
    mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    n =  4
    for i in mat:
        for j in i:
            print(j,end=" ")
        print()

    mat = rotateMatrix(mat,n)

    for i in mat:
        for j in i:
            print(j,end=" ")
        print()