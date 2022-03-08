import re
m = re.search(r"([0-9A-Za-z])\1",input())
print(m.group(1) if m else -1)


# \1 is the back reference  which checks if the character id already present