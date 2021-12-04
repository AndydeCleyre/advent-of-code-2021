#!/bin/env python3
from collections import Counter

columns = []

with open('input.txt') as infile:
    for line in infile:
        for i, digit in enumerate(reversed(line.strip())):
            if i >= len(columns):
                columns.append(Counter())
            columns[i][digit] += 1

gamma_rate = ''.join(
    digit.most_common(1)[0][0]
    for digit in reversed(columns)
)

epsilon_rate = ''.join(
    {'0': '1', '1': '0'}[d]
    for d in gamma_rate
)

print(int(gamma_rate, 2) * int(epsilon_rate, 2))
