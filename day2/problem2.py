
sum = 0
with open("input.txt") as f:
    lines = f.readlines()

    for line in lines:
        game, draws = line.split(": ")
        key = {"red":0,"green":0,"blue":0}
        game_no = int(game.split(" ")[1])
        f = True
        for draw in draws.split("; "):
            cubes = draw.split(", ")
            for cube in cubes:
                count, color = cube.split(" ")
                if int(count) > key[color.strip()]:
                    key[color.strip()] = int(count)
        values = key.values()
        power = 1
        for i in values:
            power *= i
        sum += power
print(sum)