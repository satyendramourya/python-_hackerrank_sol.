from itertools import product
a = list ( map(int , input().split()))
b = list ( map(int , input().split()))

print( *tuple(product(a , b)))