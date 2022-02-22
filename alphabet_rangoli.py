import string

def print_rangoli(size):
    n = size                                   #---> input 
    l1 = list(map(chr,range(97,123)))             #---> convertig number to ascii value
    m=len('-'.join(l1[n-1::-1]+l1[1:n]))            #---> getting the length of the middle line 
    for i in range(1,n):                       #---> forward for loop 
        print('-'.join(l1[n-1:n-i:-1]+l1[n-i:n]).center(m,'-'))                          #---> printing the pattern 
    for i in range(n,0,-1):                                       #---> reverse for loop 
        print('-'.join(l1[n-1:n-i:-1]+l1[n-i:n]).center(m,'-'))                        #---> printing the pattern  

if __name__ == '__main__':
    size = int(input())
    print_rangoli(size)  