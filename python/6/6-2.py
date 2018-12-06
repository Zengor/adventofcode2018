from collections import defaultdict
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return "({},{})".format(self.x,self.y)
        
data = []
with open("input.txt") as f:
    data = [Point(*map(int,line.split(','))) for line in f.read().splitlines()]
    
def manhattan_dist(a,b):
    return abs(a.x - b.x) + abs(a.y - b.y)

size = 0
for i in range(-200,600):
    for j in range(-200,600):
        curr_point = Point(i,j)
        distances = map(lambda p: manhattan_dist(curr_point, p), data)
        if sum(distances) < 10000:
            size += 1
print(size)
        
