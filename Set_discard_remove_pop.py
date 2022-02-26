n = int(input())
s = set(map(int, input().split()))
n = int(input())
for i in range(n):
    string = input().split()
    if string[0]=='pop' :
        s.pop()
    elif string[0]=='remove':
        s.remove(int(string[1]))
    elif string[0]=='discard':
        s.discard(int(string[1]))

print(sum(s))
