# 5
# 1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2 

from collections import Counter


k = int(input())
no_of_members = map(int,input().split())
noofmembers = Counter(no_of_members)

for k , v in noofmembers.items():
    if v == 1 :
        print(k)
        break
