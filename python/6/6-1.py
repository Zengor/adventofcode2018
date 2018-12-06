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

# note to self:
# going to calculate the grid of closests at a reasonably large size
# for the inputs, then do it again for a grid slightly larger.
# the largest which didn't change is the largest non-infinite
#
# this is really slow, even for this input size
# but it works, and there's no time limit
# i don't really know much about this problem to think of a clever way to do this.
# I'll maybe think about it if I try to do this one in Rust
def calc_closests(lower,higher):
    closest_from = defaultdict(int) #number of points which are closest from given data point p
    for i in range(lower,higher):
        for j in range(lower,higher):
            curr_point = Point(i,j)
            distances = map(lambda p: (p,manhattan_dist(curr_point, p)), data)
            closest = list(sorted(distances, key=lambda x: x[1]))
            if closest[0][1] == closest[1][1]:
                continue
            else:
                closest_from[closest[0][0]] += 1
    return closest_from
        
closest1 = calc_closests(-100,600)
closest2 = calc_closests(-200,700)
non_infinite = filter(lambda x: x[1] == closest2[x[0]],closest1.items())
highest = max(non_infinite, key=lambda x: x[1])
print(highest)
