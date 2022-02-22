from collections import Counter
the_number_of_shoes = int(input())
size_of_shoes =  Counter(list((map(int,input().split()))))
the_number_of_customers = int(input())
earned = 0
for i in range(the_number_of_customers) :
    size_asked , price = map(int, input().split())
    if size_of_shoes[size_asked] :
        earned += price 
        size_of_shoes[size_asked] -= 1 

print(earned)

