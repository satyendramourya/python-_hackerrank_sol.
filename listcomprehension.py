

''' question '''


if __name__ == '__main__':

    # x = int(input('number '))
    # y = int(input('number '))
    # z = int(input('number '))
    # n = int(input('number '))
    
    x = 1
    y = 1
    z = 2
    n = 3
    
    
    # print ([[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a + b + c != n ])
    
    x = [p for p in range(x+1)]            
    y = [q for q in range(y+1)]           
    z = [r for r in range(z+1)]            

    ls = [[i,j,k] for i  in x for j in y for k in z ]

    print ([l for l in ls if sum(l)!=n])
1