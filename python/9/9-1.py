from collections import deque
with open("../../inputs/day9.txt") as f:
    line = f.read().split()
    num_players = int(line[0])
    num_marbles = int(line[6])

circle = deque([0])
player_scores = [0] * num_players

def curr_player(curr_turn):
    return curr_turn % num_players

for marble in range(1, num_marbles+1):
    if marble % 23 == 0:
        player = curr_player(marble)
        circle.rotate(7)
        player_scores[player] += marble + circle.pop()
        circle.rotate(-1)
    else:
        circle.rotate(-1)
        circle.append(marble)

print(max(player_scores))

