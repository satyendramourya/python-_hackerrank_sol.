# if __name__ == '__main__':
#     # n = int(input())
#     n = 5
#     # arr = map(int, input().split())
#     ls = []
#     for i in range(n) :
#         a = int(input())
#         ls.append(a)
        
#     ls2 = set(ls) 
#     ls = list(ls2) 
#     ls.sort()
#     print(ls[-2])


if __name__ == '__main__':
    
    n = 5
    arr = map(int, input().split())
    # print(type(arr))
    ls= []
    for i in arr :
        ls.append(i)
    
    # print(ls)
    ls2 = set(ls) 
    ls = list(ls2) 
    ls.sort()
    print(ls[-2])
    