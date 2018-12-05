import string

with open("input.txt") as f:
    polymer = f.read().rstrip()

def will_react(i,j):
    return (i.islower() and i.upper() == j) or (j.islower() and j.upper() == i)

def calc_reaction(polymer):
    stack = []
    for c in polymer:
        if len(stack) == 0:
            stack.append(c)
            continue
        if will_react(stack[-1],c):
            stack.pop()
        else:
            stack.append(c)
    return len(stack)


reduced_polymers = (
    (c for c in filter(lambda x: not (x == to_filter or x.lower() == to_filter),polymer))
    for to_filter in string.ascii_lowercase)
print(min(map(calc_reaction, reduced_polymers)))
