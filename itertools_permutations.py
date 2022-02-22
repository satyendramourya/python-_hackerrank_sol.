from itertools import permutations 
a  = input().split()
l1 = []

# print( list(permutations(a[0] , 2)))
print(*[''.join(i) for i in permutations( sorted(a[0]) , int(a[1]))],sep='\n')

