with open("input.txt") as f:
    data = f.read().strip().splitlines()

answer_found = False
for i,line_i in enumerate(data):
    if answer_found:
        break
    for line_j in data[i+1:]:
        differences = 0
        for char_i,char_j in zip(line_i,line_j):
            if char_i != char_j:
                differences += 1
        if differences == 1:
            print(''.join(i for (i,j) in zip(line_i,line_j) if i==j))
            answer_found = True
            break
            
        
