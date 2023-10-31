#!/usr/bin/python3
i = 0
for c in range(25, -1, -1):
    c = i + ord('A')
    if i % 2 == 1:
        c += 32
    print("{:c}".format(c), end="")
