student , subject = input().split()
sub = []
for _ in range(int(subject)):
    sub.append(map(float , input().split()))

for i in zip(*sub):
    print(sum(i)/len(i))
