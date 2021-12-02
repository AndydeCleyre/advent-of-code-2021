#!/bin/env python3

ups = 0

with open('input.txt') as infile:
    prev = int(next(infile).strip())
    for line in infile:
        depth = int(line.strip())
        if depth > prev:
            ups += 1
        prev = depth

print(ups)
