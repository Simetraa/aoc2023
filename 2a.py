from aocd import data, submit
possible_games = []

for line in data.splitlines():
    game_id, colour_data = line.split(": ")
    game_id = game_id[5:]
    game_id = int(game_id)

    game_possible = True
    for pull in colour_data.split("; "):
        colours = dict()
        colour_and_quantity = pull.split(", ")
        for i in colour_and_quantity:
            quantity, colour = i.split(" ")
            quantity = int(quantity)
            if colour in colours:
                colours[colour] += quantity
            else:
                colours[colour] = quantity
        # 12 red cubes, 13 green cubes, and 14 blue cubes
        if colours.get("red", 0) > 12 or colours.get("green", 0) > 13 or colours.get("blue", 0) > 14:
            game_possible = False
    if game_possible:
        possible_games.append(game_id)

submit(sum(possible_games))
