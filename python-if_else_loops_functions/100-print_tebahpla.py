#!/usr/bin/python3
"""Print the ASCII alphabet in reverse, alternating lower/upper."""
for i in range(25, -1, -1):
    c = 122 - i
    if i % 2 == 0:
        print("{:c}".format(c), end="")
    else:
        print("{:c}".format(c - 32), end="")
        