def matrix_row(matrix,i,m):
    for j in range(m):
        if matrix[i][j] != 0:
            matrix[i][j] = -1
    return matrix

def matrix_col(matrix,n,j):
    for i in range(n):
        if matrix[i][j] != 0:
            matrix[i][j] = -1
    return matrix

def zeroMatrix(matrix, n, m):
    # Write your code here.
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                matrix = matrix_row(matrix,i,m)
                matrix = matrix_col(matrix,n,j)
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == -1:
                matrix[i][j] = 0
    return matrix

if __name__ == "__main__":
    mat = [[2, 4, 3],[1, 0, 0]]
    n,m = 2, 3
    mat = zeroMatrix(mat,n,m)
    for i in range(n):
        for j in range(m):
            print(mat[i][j],end=" ")
        print()

