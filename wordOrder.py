from collections import OrderedDict
order = OrderedDict()
for i in range(int(input())):
    a = input()
    order.setdefault(a,0)
    order[a]+=1
    
print(len(order))
print(*order.values())
