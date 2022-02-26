'''sol _1'''
# a = set(map(int,input().split()))
# n = int(input())
# count = 0 
# for i in range(n):
#     b = set(map(int,input().split()))
#     if a.issuperset(b):
#         count+=1
# print(count == n)

''' sol_2'''
a = set(input().split())
print(all([a.issuperset(set(input().split()))for _ in range(int(input()))]))
