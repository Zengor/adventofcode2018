import re
from itertools import starmap
class Particle:
    def __init__(self, x, y, v_x, v_y):
        self.x = x
        self.y = y
        self.v_x = v_x
        self.v_y = v_y
    def x_at_sec(self, sec):
        return self.x + sec * self.v_x
    def y_at_sec(self, sec):
        return self.y + sec * self.v_y
    def pos_at_sec(self, sec):
        return self.x_at_sec(sec), self.y_at_sec(sec)
    
with open("../../inputs/day10.txt") as f:
    particles = [Particle(*map(int, re.findall(r'-?\d+', line))) for line in f.read().splitlines()]

# given the xs and ys of the current second, find the length of the sides of the bounding box
def get_bound_box(xs, ys):
    max_x, min_x, max_y, min_y = xs[0], xs[0], ys[0], ys[0]
    for x, y in zip(xs, ys):
        max_x = max(x, max_x)
        min_x = min(x, min_x)
        max_y = max(y, max_y)
        min_y = min(y, min_y)
    return (max_x, min_x, max_y, min_y)

def get_bound_box_size(xs, ys):
    max_x, min_x, max_y, min_y = get_bound_box(xs, ys)
    return (max_x - min_x) + (max_y - min_y)

def get_positions_at_sec(particles, sec):
    return zip(*map(lambda p: p.pos_at_sec(sec), particles))

# find bounding box sizes
# get smallest one (if the smallest one isn't the one with the message we can check the
# others in sorted order
positions = ( get_positions_at_sec(particles,sec) for sec in range(100000) )
boxes = enumerate(starmap(get_bound_box_size, positions))
smallest_sec, smallest_size = min(boxes, key=lambda x: x[1])
print(smallest_sec)
print('-')
def print_particles(particles, sec):
    xs, ys = get_positions_at_sec(particles, sec)
    max_x, min_x, max_y, min_y = get_bound_box(xs, ys)
    points = set(zip(xs, ys))
    for y in range(min_y, max_y+1):
        for x in range(min_x, max_x+1):
            if (x,y) in points:
                print('#', end='')
            else:
                print('_', end='')
        print('')
        
print_particles(particles, smallest_sec)
print("at sec ", smallest_sec)
