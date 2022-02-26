from collections import defaultdict
n , m = map(int,input().split())
dictl  = defaultdict(list)
for i in range(n):
    group_A=input().rstrip()
    dictl[group_A].append(i+1)

for i in range(m):
    group_B = input().rstrip()
    if group_B in dictl:
        print(' '.join(map(str,dictl[group_B])))
    else:
        print('-1')

