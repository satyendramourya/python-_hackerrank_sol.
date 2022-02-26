for i in range(int(input())):
    
    try:
        b ,c =map(int,input().split())
        print(b//c)
    except BaseException as e :
        print('Error Code:',e)