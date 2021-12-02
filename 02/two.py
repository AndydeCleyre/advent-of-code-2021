#!/bin/env python3

location = {
    'position': 0,
    'depth': 0,
    'aim': 0
}
dirs = {
    'forward': (
        ('position', int),
        ('depth', lambda x: int(x) * location['aim'])
    ),
    'down': (('aim', int),),
    'up': (('aim', lambda x: -int(x)),)
}

with open('input.txt') as infile:
    for line in infile:
        direction, distance = line.split()
        for axis, parse in dirs[direction]:
            location[axis] += parse(distance)

print(location['position'] * location['depth'])
