with open("input.txt") as f:
    data = list(map(int,f.read().split()))

# returns tuple of the total length traversed and the value of the header node 
# (see problem description for definition of value
def traverse_value(data_slice):
    num_children = data_slice[0]
    num_metadata = data_slice[1]
    if num_children == 0:
        total = sum(data_slice[2:2+num_metadata])
        return (2+num_metadata, total)
    values = []
    curr_pos = 2
    for i in range(num_children): 
        child_length, child_value = traverse_value(data_slice[curr_pos:])
        curr_pos += child_length
        values.append(child_value)
    total = 0
    length = curr_pos+num_metadata
    # data reference must be non-zero and less than the number of children
    valid_metadata = (x for x in data_slice[curr_pos:length] if x > 0 and x <= num_children)
    for metadata in valid_metadata:
        total += values[metadata-1]    
    return (length, total)

_, value = traverse_value(data)
print(value)
