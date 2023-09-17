# li = [2,5,1,3,0]

#TimeComplexity : O(nlogn)
# li.sort()
# print(li[-2])

#TimeComplexity : O(n)
# ma = li[0]
# mi = li[0]
# for i in li[1:]:
#     if ma < i:
#         ma = i
#     if mi > i:
#         mi = i
# print(ma,mi)
# sma = li[0]
# smi = li[0]
# for i in li:
#     if i != ma and i != mi:
#         if sma < i:
#             sma = i
#         if smi > i:
#             smi = i
# print(sma,smi)
# li = [2,5,1,3,0]
li = [1,2, 3, 4, 5, 6, 7, 8, 9, 10 ]
ma = float('-inf')
mi = float('inf')
sma = float('-inf')
smi = float('inf')


for i in li:
    if mi > i:
        smi = mi
        mi = i
    if smi > i and mi != i:
        smi = i
    if ma < i:
        sma = ma
        ma = i
    if sma < i and ma != i:
        sma = i

print(ma,mi,sma,smi)