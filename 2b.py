import math
from aocd import data, submit

powers = []

for line in data.splitlines():
    game_id, colour_data = line.split(": ")
    game_id = game_id[5:]
    game_id = int(game_id)

    min_pull = dict()
    for p in colour_data.split("; "):
        colour_and_quantity = p.split(", ")
        for i in colour_and_quantity:
            quantity, colour = i.split(" ")
            quantity = int(quantity)
            if colour in min_pull:
                min_pull[colour] = max(quantity, min_pull[colour])
            else:
                min_pull[colour] = quantity

    powers.append(math.prod(min_pull.values()))

submit(sum(powers))
