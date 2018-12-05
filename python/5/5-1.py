with open("input.txt") as f:
    polymer = f.read().rstrip()

def will_react(i,j):
    return (i.islower() and i.upper() == j) or (j.islower() and j.upper() == i)

stack = []
for c in polymer:
    if len(stack) == 0:
        stack.append(c)
        continue
    if will_react(stack[-1],c):
        stack.pop()
    else:
        stack.append(c)
print(''.join(stack))
print(len(stack))
