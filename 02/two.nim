import std/strutils

var
  position = 0
  depth = 0
  aim = 0
  direction: string
  distance: string
  idistance: int

for line in "input.txt".lines:
  (direction, distance) = line.split
  idistance = distance.parse_int
  case direction
  of "forward":
    position.inc idistance
    depth.inc idistance * aim
  of "down":
    aim.inc idistance
  of "up":
    aim.dec idistance

(position * depth).echo
