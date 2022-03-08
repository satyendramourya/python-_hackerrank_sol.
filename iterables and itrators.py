from itertools import combinations
n ,s,p = int(input()) , input().split(),  int(input())
z =list(combinations(s,p))
fav_combinations = 0
for i in z:
    if 'a' in i :
        fav_combinations += 1

print(fav_combinations/len(z))