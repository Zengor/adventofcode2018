from collections import defaultdict

children_of = defaultdict(list)
parents_of = defaultdict(list)
num_nodes = 0

with open("../../inputs/day7.txt") as f:    
    for line in f:
        split = line.split()
        node_from = split[1]
        node_to = split[7]
        if node_from not in children_of and node_from not in parents_of:
            num_nodes += 1
        if node_to not in children_of and node_to not in parents_of:
            num_nodes += 1
        children_of[node_from].append(node_to)
        parents_of[node_to].append(node_from)

visible = set(filter(lambda x: len(parents_of[x]) == 0, children_of.keys()))
sorted_list = []
while visible:
    print(''.join(sorted_list))
    print(sorted(visible))
    curr = sorted(visible)[0]
    visible.remove(curr)
    sorted_list.append(curr)
    for child in children_of[curr]:
        parents_of[child].remove(curr)
        if len(parents_of[child]) == 0:
            visible.add(child)
    
print(''.join(sorted_list))
