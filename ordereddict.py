# rpartition() method searches for the last occurrence of a specified string, and splits the string into a tuple containing three elements.

from collections import OrderedDict 
a = OrderedDict()
for i in range(int(input())):
    item , blank , price  = input().rpartition(' ')
    a[item] = a.get(item,0)+int(price)             #----------> (item , 0) item is item name , 0 is the default value ,,,,,,,, adding the price 
for item , qu  in  a.items():
    print(item , qu)