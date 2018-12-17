from collections import defaultdict
from string import ascii_uppercase
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
curr_time = -1
tasks_done = 0
workers = [('a',-1)] * 5
while tasks_done < num_nodes:
    if curr_time % 1 == 0:
        print(visible)
        print(workers)
    curr_time += 1
    for i in range(len(workers)):
        workers[i] = (workers[i][0], workers[i][1] - 1)
        if workers[i][1] == 0:
            tasks_done += 1
            for child in children_of[workers[i][0]]:
                parents_of[child].remove(workers[i][0])
                if len(parents_of[child]) == 0:
                    visible.add(child)
    for worker_free,_ in filter(lambda x: x[1][1] <= 0, enumerate(workers)):
        if not visible:
            break
        task_to_do = min(visible)
        visible.remove(task_to_do)
        time = 60 + ascii_uppercase.index(task_to_do) + 1
        workers[worker_free] = (task_to_do, time)
print(curr_time)
