with open("input.txt") as f:
    data = list(map(int,f.read().split()))

# returns tuple of the total length traversed and the sum of metadata of header + its children
def traverse(data_slice):
    num_children = data_slice[0]
    num_metadata = data_slice[1]
    total = 0
    curr_pos = 2
    for i in range(num_children):
        child_length, child_metadata = traverse(data_slice[curr_pos:])
        curr_pos += child_length
        total += child_metadata
    length = curr_pos + num_metadata
    total += sum(data_slice[curr_pos:length])
    return (length, total)

_, total = traverse(data)
print(total)
