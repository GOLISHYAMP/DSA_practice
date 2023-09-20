# arr = [1, 5, 6, 8 ,9]
# another = list(map(lambda x : str(x),arr))
# print(' '.join(another))

# from itertools import permutations
from itertools import combinations
li = []
li.append(int(input()))
li.append(int(input()))
li.append(int(input()))
n = int(input())
# final = list(permutations(li,3))
final = list(combinations(li,2))
print(final)