def majorityElement(v):
    # Write your code here
    # n = len(v)
    # for i in v:
    #     count = 0
    #     for j in range(n):
    #         if i == v[j]:
    #             count += 1
    #     if count > int(n/2):
    #         return i
    # return n
    n = len(v)
    my_dic = {}
    for i in v:
        my_dic[i] = my_dic.get(i,0) + 1
    val = max(my_dic.values())
    if val > int(n/2):
        for i in my_dic:
            if my_dic[i] == val:
                return i
    else:
        return n
    
if __name__ == "__main__":
    print(majorityElement([2, 2, 1, 3, 1, 1, 3, 1, 1]))