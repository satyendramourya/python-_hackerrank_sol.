from itertools import combinations
a , b = input().split()
for i in range(int(b)):
    print(*map(''.join,combinations(sorted(a),i+1)),sep = '\n')