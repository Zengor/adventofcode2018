frequency = 0
with open("input-1.txt") as f:
    frequency = sum(int(line) for line in f)
print(frequency)
