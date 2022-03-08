from datetime import datetime

def delta(t1, t2):
    f= '%a %d %b %Y %H:%M:%S %z'
    t1 = datetime.strptime(t1, f)
    t2 = datetime.strptime(t2, f)
    diff = (t2-t1).total_seconds()
    return abs(int(diff))


for _ in range(int(input())):
    print(delta(input(), input()))
