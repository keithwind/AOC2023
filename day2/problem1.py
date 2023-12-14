key = {"red":12,"green":13,"blue":14}
sum = 0
with open("input.txt") as f:
    lines = f.readlines()

    for line in lines:
        game, draws = line.split(": ")
        game_no = int(game.split(" ")[1])
        f = True
        for draw in draws.split("; "):
            cubes = draw.split(", ")
            for cube in cubes:
                count, color = cube.split(" ")
                if int(count) > key[color.strip()]:
                    f = False
        if(f): sum+= game_no
print(sum)

                
