import re

GAME_LIMITS = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

def get_game_id(line: str) -> int:
    identifier = line.split(':')[0]
    game_id = re.findall('[0-9]+', identifier)[0]
    return int(game_id)

def get_colour_count(cube_set: list[str]) -> list():
    colour_count = []
    for cubes in cube_set.split(','):
        total = int(re.findall('[0-9]+', cubes)[0])
        colour = re.findall('[a-z]+', cubes)[0]
        colour_count.append((colour, total))
    return colour_count

def game_is_possible(line: str) -> bool:
    revealed = line.split(':')[1]
    for cube_set in revealed.split(';'):
        colour_count = get_colour_count(cube_set=cube_set)
        for cubes in colour_count:
            if cubes[1] > GAME_LIMITS[cubes[0]]:
                return False
    return True


def part_one(filepath="./inputs/day02.txt"):
    result = 0
    with open(filepath, 'r') as f:
        line = f.readline().strip()
        while line:
            possible = game_is_possible(line)
            if possible:
                game_id = get_game_id(line)
                result += game_id
            line = f.readline().strip()
    return result

def get_minimum_colours(line: str) -> dict:
    minimum_colours = {}
    revealed = line.split(':')[1]
    pulled_cube_sets = [get_colour_count(cube_set=cube_set) for cube_set in revealed.split(';')]
    for cube_set in pulled_cube_sets:
        for cubes in cube_set:
            colour = cubes[0]
            pulled = int(cubes[1])
            minimum = minimum_colours.get(colour, 0)
            minimum_colours[colour] = max(pulled, minimum)
    return minimum_colours

def get_power(line: str) -> int:
    minimum_colours = get_minimum_colours(line)
    power = 1
    for colour in minimum_colours.values():
        power *= colour
    return power


def part_two(filepath="./inputs/day02.txt"):
    result = 0
    with open(filepath, 'r') as f:
        line = f.readline().strip()
        while line:
            power = get_power(line)
            result += power
            line = f.readline().strip()
    return result