# Input Format: N = 6
# Result:   
# 6 6 6 6 6 6 6 6 6 6 6 
# 6 5 5 5 5 5 5 5 5 5 6 
# 6 5 4 4 4 4 4 4 4 5 6 
# 6 5 4 3 3 3 3 3 4 5 6 
# 6 5 4 3 2 2 2 3 4 5 6 
# 6 5 4 3 2 1 2 3 4 5 6 
# 6 5 4 3 2 2 2 3 4 5 6 
# 6 5 4 3 3 3 3 3 4 5 6 
# 6 5 4 4 4 4 4 4 4 5 6 
# 6 5 5 5 5 5 5 5 5 5 6 
# 6 6 6 6 6 6 6 6 6 6 6

# first method GOOD Easy way but consumes more space!

# n = int(input())
# array = []
# for i in range(n):
#     arr = []
#     pr = (n*2)-1
#     temp = 0
#     for j in reversed(range((n-i),n+1)):
#         print(j,end= " ")
#         arr.append(j)
#         temp = j
#     for k in range(pr-((i+1)*2)):
#         print(temp,end=" ")
#         arr.append(temp)
#     if i == n-1:
#         for t in range(temp+1,n+1):
#             print(t,end=" ")
#     else:
#         for t in range(temp,n+1):
#             print(t,end=" ")
#             arr.append(t)
#     if len(arr) > n+1:
#         array.append(arr)
#     print()

# for i in reversed(array):
#     temp = list(map(lambda x : str(x), i))
#     print(" ".join(temp))
###################################################################################

# Second method difficult way but space efficient

n = int(input())
for i in range(n):
    pr = (n*2)-1
    temp = 0
    for j in reversed(range((n-i),n+1)):
        print(j,end= " ")
        temp = j
    for k in range(pr-((i+1)*2)):
        print(temp,end=" ")
    if i == n-1:
        for t in range(temp+1,n+1):
            print(t,end=" ")
    else:
        for t in range(temp,n+1):
            print(t,end=" ")
    print()



for i in range(1,n):
    temp = 0
    for j in reversed(range(i+1,n+1)):
        print(j, end=" ")
        temp = j
    for k in range((i*2)-1):
        print(j, end=" ")
    for t in range(i+1,n+1):
        print(t,end=" ")
    
    print()


