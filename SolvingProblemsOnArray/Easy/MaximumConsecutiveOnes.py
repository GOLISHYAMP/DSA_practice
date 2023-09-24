def traffic(n, m, vehicle):
    # Write your code here.
    k = 0
    ma = 0
    while k < n:
        temp = []
        for i in vehicle:
            temp.append(i)
        # print("temp = ",temp)
        t = m
        for i in range(k,n):
            if temp[i] == 0 and t > 0:
                temp[i] = 1
                t -= 1
        # prev = 0
        s = 0
        # print(temp)
        for i in range(n):
            if temp[i] == 1: 
                # prev = 1
                s += 1
                if i == n-1:
                    if ma < s:
                        ma = s
            else:
                # prev = 0
                if ma < s:
                    ma = s
                s = 0
                
        k += 1
    return ma
        

#3 1
# 0 1 1  
# output should be 3

# 6 3
# 0 1 0 0 1 0
#output shoud be 5

if __name__ == "__main__":
    arr = [0,1,0,0,1,0]
    print(traffic(len(arr),3,arr))
