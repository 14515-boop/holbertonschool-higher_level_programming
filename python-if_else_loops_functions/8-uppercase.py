#!/usr/bin/python3
def uppercase(text):
    """print a string in uppercase using ASCII conversion only."""
    result = ""
    for ch in text:
        if 'a' <= ch <= 'z':
            result += chr(ord(ch) - 32)
        else:
            result += ch
    print("{}".format(result))