#!/usr/bin/python3
"""Print the ASCII alphabet in reverse, alternating lower/upper."""
for i in range(25, -1, -1):
    c = 122 - i
    print("{:c}".format(c - (32 if i % 2 else 0)), end="")
