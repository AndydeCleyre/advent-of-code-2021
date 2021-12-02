#!/bin/env python3

ups = 0

with open('input.txt') as infile:
    a, b, c = (
        int(next(infile).strip()),
        int(next(infile).strip()),
        int(next(infile).strip())
    )
    prev = a + b + c
    while True:
        try:
            a, b, c = b, c, int(next(infile).strip())
        except StopIteration:
            print(ups)
            break
        else:
            total = a + b + c
            if total > prev:
                ups += 1
            prev = total
