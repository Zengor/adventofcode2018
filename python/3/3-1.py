from itertools import product

with open("../../inputs/day3.txt") as f:
    data = f.read().splitlines()

class Rect:
    def __init__(self, x,y, w, h):
        self.left = x
        self.top = y
        self.right = x + w
        self.bottom = y + h
    

def parse_claim(claim):
    split = claim.split()
    x, y = split[2].split(',')
    w, h = split[3].split('x')
    return Rect(int(x), int(y[:-1]), int(w), int(h))

claims = []
for c in data:
    claims.append(parse_claim(c))


def detect_collision(a,b):
    return (a.left < b.right and
            a.right > b.left and
            a.top < b.bottom and
            a.bottom > b.top)

# (x,y) point at the top left of the intersection
def overlap_start(a,b):
    return (max(a.left,b.left),max(a.top,b.top))

# return width and height of the intersection
def overlap_area(a,b):
    w = min(a.right,b.right) - max(a.left, b.left)
    h = min(a.bottom,b.bottom) - max(a.top,b.top)
    return  (w,h)
    
    
overlapped_tiles = set()

for i, claim_i in enumerate(claims):
    for claim_j in claims[i+1:]:
        if detect_collision(claim_i,claim_j):
            start_x, start_y = overlap_start(claim_i,claim_j)
            width, height = overlap_area(claim_i, claim_j)
            for x,y in product(range(start_x, start_x+width), range(start_y, start_y + height)):
                overlapped_tiles.add((x,y))
print(len(overlapped_tiles))
            
