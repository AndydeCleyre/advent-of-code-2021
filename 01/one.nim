import std/strutils

var
  ups = 0
  prev: int
  depth: int
  first = true

for line in "input.txt".lines:
  if first:
    prev = line.parse_int
    first = false
  else:
    depth = line.parse_int
    if depth > prev:
      ups.inc
    prev = depth

ups.echo
