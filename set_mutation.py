n = int(input())
set1 = set(map(int,input().split()))
for i in range(int(input())):
    a , b = input().split()
    set2 = set(map(int,input().split()))
    if a=="intersection_update":
        set1.intersection_update(set2)
    elif a=="update":
        set1.update(set2)
    elif a=="symmetric_difference_update":
        set1.symmetric_difference_update(set2)
    elif a=="difference_update":
        set1.difference_update(set2)
    

print(sum(set1))
