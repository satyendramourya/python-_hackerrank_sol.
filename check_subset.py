testcases = int(input())
for i in range(testcases) :
    nA = int(input())
    a = set(map(int,input().split()))
    nB = int(input())
    b = set(map(int,input().split()))
    
    print(a.issubset(b))