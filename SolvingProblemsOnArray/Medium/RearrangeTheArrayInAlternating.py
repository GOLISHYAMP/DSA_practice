from typing import *

def alternateNumbers(a):
    # Write your code here.
    # posi_list = []
    # neg_list = []
    # for i in a:
    #     if i < 0:
    #         neg_list.append(i)
    #     else:
    #         posi_list.append(i)
    # final_list = []
    # i,j = 0,0
    # # k = 0
    # while(i < len(posi_list) and j < len(neg_list)):
    #     final_list.append(posi_list[i])
    #     # k += 1
    #     i += 1
    #     final_list.append(neg_list[j])
    #     # k += 1
    #     j += 1

    # while(i < len(posi_list)):
    #     final_list.append(posi_list[i])

    #     # k += 1
    #     i += 1
    # while(j < len(neg_list)):
    #     final_list.append(neg_list[j])
    #     # k += 1
    #     j += 1
    # return final_list
    n = len(a)
    arr = [0] * n
    posIndex,negIndex = 0,1
    for i in range(n):
        if a[i] < 0:
            arr[negIndex] = a[i]
            negIndex += 2
        else:
            arr[posIndex] = a[i]
            posIndex += 2
    return arr


if __name__ == "__main__":
    print(alternateNumbers([1, 2, -3, -1, -2, 3]))