def printSpiralManner(mat,n):
    min = 0
    max = n-1
    # i = -1
    i = 0
    j = -1
    cnt = 0
    if n % 2 == 0:
        rounding = n-2
    else: 
        rounding = n-1
    while (cnt < rounding):
        while(j < max):
            j += 1
            print(mat[min][j],end=" ")
        # j -= 1
        # i += 1
        while(i < max):
                i += 1
                print(mat[i][max],end=" ")
        # print("value of x : ",i)
        # print("value of y : ",j)

        while(j > min):
                j -= 1
                print(mat[max][j],end=" ")

        # i -= 1
        while(i > min+1):
                i -= 1
                print(mat[i][j],end=" ")

        #  Second round  increase the min and decrease the max
        min += 1
        max -= 1
        cnt += 1
    # while(j < max):
    #     j += 1
    #     print(mat[min][j],end=" ")
    
    # # i += 1
    # while(i < max):
    #         i += 1
    #         print(mat[i][max],end=" ")

    # while(j > min):
    #      j -= 1
    #      print(mat[max][j],end=" ")
    
    # while(i > min+1):
    #      i -= 1
    #      print(mat[i][j],end=" ")

if __name__ == "__main__":
    # mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    # mat = [[1,2,3],[4,5,6],[7,8,9]]
    # mat = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
    mat = [[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18],[19,20,21,22,23,24],[25,26,27,28,29,30],[31,32,33,34,35,36]]
    for i in mat:
        for j in i:
            print(j,end=" ")
    print()

    printSpiralManner(mat,len(mat[0]))
