import re
for i in range(int(input())):
    print(bool(re.search( r'^[+-]?[0-9]*\.[0-9]+$',input().strip())))


    #  ^  --> starts with
    #  [+-]  --> either + or -
    #  \?   --> Zero or one occurrences
    #  [0-9] -->  set of no, from 0-9
    #  * --> zero or more occurence
    #  \ --> skip character
    #  + --> one or more occurence 
    #  $ --> ends with 