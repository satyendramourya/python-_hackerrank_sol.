def cube(x): return x**3


def fibonacci(n):
    ls = [ 0 , 1 ] 
    [ls.append(ls[a-2] + ls[a-1]) for a in range( 2 , n) ]
    return ls[0:n]


    # ls[0:n] --> returns empty lst when the n is 0 and [0] when the n is 1 


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))     # implementiing the  lambda function on fibomacci list



