from itertools import cycle

frequency = 0
found = { 0 }
result = 0

with open("input-1.txt") as f:
    for line in cycle(f):
        frequency += int(line)
        if frequency in found:
            print(frequency)
            break
        found.add(frequency)
