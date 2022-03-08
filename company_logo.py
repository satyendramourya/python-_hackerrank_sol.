from collections import Counter


# for c in Counter(sorted(input())).most_common(3):
#     print(*c)

[print(*c) for c in Counter(input()).most_common(3)]