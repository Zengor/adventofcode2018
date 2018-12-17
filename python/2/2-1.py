from collections import Counter
num_two = 0
num_three = 0

def has_any_of_count(counter, num):
    return any(map((lambda c: c == num), counter.values()))

with open("../../inputs/day2.txt") as f:
    for line in f:
        c = Counter(line)
        if has_any_of_count(c, 2):
            num_two += 1
        if has_any_of_count(c, 3):
            num_three += 1

print(num_two * num_three)
        
