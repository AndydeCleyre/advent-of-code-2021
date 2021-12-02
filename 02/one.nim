import std/strutils

var
  position = 0
  depth = 0
  direction: string
  distance: string

for line in "input.txt".lines:
  (direction, distance) = line.split
  case direction
  of "forward":
    position.inc distance.parse_int
  of "down":
    depth.inc distance.parse_int
  of "up":
    depth.dec distance.parse_int

(position * depth).echo
