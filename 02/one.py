#!/bin/env python3

location = {'position': 0, 'depth': 0}
dirs = {
    'forward': ('position', int),
    'down': ('depth', int),
    'up': ('depth', lambda x: -int(x))
}

with open('input.txt') as infile:
    for line in infile:
        direction, distance = line.split()
        axis, parse = dirs[direction]
        location[axis] += parse(distance)

print(location['position'] * location['depth'])
