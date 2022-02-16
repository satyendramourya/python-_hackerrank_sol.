'''
Sample Input 0

12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
Sample Output 0

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]

'''

if __name__ == '__main__':
    N =int(input())
    ls=[]
    count=0
    while(count<N):
        a=input().split()
        
        
        if a[0]=='insert':
            ls.insert(int(a[1]),int(a[2]))
        
        elif a[0]=='print':
            print(ls)

        elif a[0]=='remove':
            ls.remove(int(a[1]))
        
        elif a[0] =='append':
            ls.append(int(a[1]))
        
        elif a[0]=='sort':
            ls.sort()
        
        elif a[0]=='pop':
            ls.pop()
        
        elif a[0]=='reverse':
            ls.reverse()

        count += 1


    

