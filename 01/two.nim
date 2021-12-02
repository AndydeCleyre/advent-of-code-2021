import std/strutils
import sequtils

var
  ups = -1
  prev = -1
  total: int

let
  all_lines = "input.txt".lines.to_seq

for i, line in all_lines.pairs:
  try:
    total = line.parse_int +
      all_lines[i + 1].parse_int +
      all_lines[i + 2].parse_int
  except IndexDefect:
    ups.echo
    break
  if total > prev:
    ups.inc
  prev = total
