from itertools import product

with open("input.txt") as f:
    data = f.read().splitlines()
    
n_ids = len(data)
class Rect:
    def __init__(self, x,y, w, h, claim_id):
        self.left = x
        self.top = y
        self.right = x + w
        self.bottom = y + h
        self.claim_id = claim_id
    

def parse_claim(claim):
    split = claim.split()
    claim_id = int(split[0][1:])
    x, y = split[2].split(',')
    w, h = split[3].split('x')
    return Rect(int(x), int(y[:-1]), int(w), int(h), claim_id)

claims = []
for c in data:
    claims.append(parse_claim(c))


def detect_collision(a,b):
    return (a.left < b.right and
            a.right > b.left and
            a.top < b.bottom and
            a.bottom > b.top)
   
overlapped_claims = set()

for i, claim_i in enumerate(claims):
    for claim_j in claims[i+1:]:
        if detect_collision(claim_i,claim_j):
                overlapped_claims.add(claim_j.claim_id)
                overlapped_claims.add(claim_i.claim_id)
                
for i in range(1,n_ids+1):
    if i not in overlapped_claims:
        print(i)
        break

            
