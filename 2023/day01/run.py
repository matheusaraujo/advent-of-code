import sys

from problem1 import problem1
from problem2 import problem2

lines = []

for line in sys.stdin:
    lines.append(line)

print("problem1: %d" % problem1(lines))
print("problem2: %d" % problem2(lines))