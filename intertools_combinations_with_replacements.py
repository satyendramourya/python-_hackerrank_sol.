from itertools import combinations
a , b = input().split()
print(*map(''.join,combinations(sorted(a),int(b))),sep = '\n')