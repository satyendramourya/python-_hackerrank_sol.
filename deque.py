# from collections import deque
# d = deque()
# d.append(1)
# print(d)
# deque([1])
# d.appendleft(2)
# print(d)
# deque([2, 1])
# d.clear()
# print(d)
# deque([])
# d.extend('1')
# print(d)
# deque(['1'])
# d.extendleft('234')
# print(d)
# deque(['4', '3', '2', '1'])
# d.count('1')
# 1
# d.pop()
# '1'
# print(d)
# deque(['4', '3', '2'])
# d.popleft()
# '4'
# print(d)
# deque(['3', '2'])
# d.extend('7896')
# print(d)
# deque(['3', '2', '7', '8', '9', '6'])
# d.remove('2')
# print(d)
# deque(['3', '7', '8', '9', '6'])
# d.reverse()
# print(d)
# deque(['6', '9', '8', '7', '3'])
# d.rotate(3)
# print(d)
# deque(['8', '7', '3', '6', '9'])

from collections import deque
a = int(input())
d = deque()
for i in range(a):
    b = input().split()
    if b[0] == 'pop':
        d.pop()
        
    elif b[0] == 'popleft':
        d.popleft()
        
    elif b[0] == 'append':
        d.append(int(b[1]))
        
    elif b[0] == 'appendleft':
        d.appendleft(int(b[1]))
        
print(*[items for items in d])




















