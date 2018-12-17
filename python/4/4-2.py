from datetime import datetime
from collections import defaultdict, Counter
# events
WAKE = 1
SLEEP = 2
SHIFT_START = 3

class Entry:
    def __init__(self, timestamp, event, guard_id):
        self.timestamp = timestamp
        self.event = event        
        self.guard_id = guard_id
    def time(self):
        return self.timestamp
    
def parse_entry(log_entry):
    split = log_entry.split()
    y, m, d = map(int,split[0][1:].split('-'))
    h, minute = map(int,split[1][:-1].split(':'))
    timestamp = datetime(y, m, d, h, minute)
    guard_id = 0
    if split[2] == "falls":
        event = SLEEP
    if split[2] == "wakes":
        event = WAKE
    if split[2] == "Guard":
        event = SHIFT_START
        guard_id = int(split[3][1:])
    return Entry(timestamp, event, guard_id)

with open("../../inputs/day4.txt") as f:
    entries = map(parse_entry, f.read().splitlines())
    
guard_id = 0
sleep_start = 0
slept_time = defaultdict(Counter)

for entry in sorted(entries, key=Entry.time):    
    if entry.event == SHIFT_START:
        guard_id = entry.guard_id
    if entry.event == SLEEP:
        sleep_start = entry.timestamp.minute
    if entry.event == WAKE:
        slept_time[guard_id].update(range(sleep_start, entry.timestamp.minute))

highest = max(slept_time.items(), key=(lambda i: i[1].most_common(1)[0][1]))
print(highest[0] * highest[1].most_common(1)[0][0])
