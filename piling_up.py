# STDIN        Function
# -----        --------
# 2            T = 2
# 6            blocks[] size n = 6
# 4 3 2 1 3 4  blocks = [4, 3, 2, 1, 3, 4]
# 3            blocks[] size n = 3
# 1 3 2        blocks = [1, 3, 2]


'''easy '''
from collections import deque
for _ in range(int(input())) :
    en =int(input())
    old_block = deque(map(int,input().split()))
    new_block = []
    for i in range(len(old_block) ):
        if old_block[-1] > old_block[0]:
            new_block.append(old_block.pop())
        else : 
            new_block.append(old_block.popleft())

    print(new_block)
    if new_block == sorted(new_block)[::-1]:
        print('Yes')
    else :
        print('No')



'''shorter'''
from collections import deque
for _ in range(int(input())) :
    new_block = []
    en , old_block  = int(input()), deque(map(int,input().split()))
    [new_block.append(old_block.pop() if old_block[-1] > old_block[0] else old_block.popleft() )for i in range(en)]
    print('Yes' if new_block == sorted(new_block)[::-1] else 'No' )
