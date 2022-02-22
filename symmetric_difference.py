
a = int(input())
set1 = set(map(str,input().split(' ')))
b = int(input())
set2 = set(map(str,input().split(' ')))

# p = set1.difference(set2)
# q = set2.difference(set1)
# r = p.union(q)
# print("\n".join(sorted(r , key= int)))

print("\n".join(sorted(set1.difference(set2).union(set2.difference(set1)) , key= int)))