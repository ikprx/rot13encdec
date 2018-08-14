#!/usr/bin/env python
import sys

def rot13(i):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    output = ""
    for c in i:
        if c in alphabet:
            newindex = (alphabet.index(c) + 13) % len(alphabet)
            output += alphabet[newindex]
        elif c.lower() in alphabet:
            newindex = (alphabet.index(c.lower()) + 13) % len(alphabet)
            output += alphabet[newindex].upper()
        else:
            output += c
    return output

print(rot13(input("Enter the input: ")))
