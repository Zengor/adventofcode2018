frequency = 0
with open("../../inputs/day1.txt") as f:
    frequency = sum(int(line) for line in f)
print(frequency)
