from typing import *

def alternateNumbers(a):
    # Write your code here.
    posi_list = []
    neg_list = []
    for i in a:
        if i < 0:
            neg_list.append(i)
        else:
            posi_list.append(i)
    final_list = []
    i,j = 0,0
    # k = 0
    while(i < len(posi_list) and j < len(neg_list)):
        final_list.append(posi_list[i])
        # k += 1
        i += 1
        final_list.append(neg_list[j])
        # k += 1
        j += 1

    while(i < len(posi_list)):
        final_list.append(posi_list[i])

        # k += 1
        i += 1
    while(j < len(neg_list)):
        final_list.append(neg_list[j])
        # k += 1
        j += 1
    return final_list


if __name__ == "__main__":
    print(alternateNumbers([1, 2, -3, -1, -2, 3]))