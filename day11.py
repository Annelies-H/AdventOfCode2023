from collections import namedtuple

Coordinate = namedtuple("Coordinate", ["x", "y"])


def expand_space(space):
    expanded_space = []
    empty_columns = [i for i in range(0, len(space[0]))]

    for row in space:
        expanded_space.append(row)
        if not '#' in row:
            # expand vertically
            #TODO use a copy because now its referring to the same data....
            expanded_space.append(row)
        else:
            for column in empty_columns:
                if row[column] == '#':
                    empty_columns.remove(column)

    empty_columns.reverse()

    for row in expanded_space:
        for column in empty_columns:
            # expand horizontally
            row.insert(column, '.')

    return expanded_space


def get_coordinates(space):
    coordinates = []
    for y, row in enumerate(space):
        for x, point in enumerate(row):
            if point == "#":
                coordinates.append(Coordinate(x, y))
    return coordinates

def compute_total_distance(coordinates):
    total_distance = 0
    for index, galaxy in enumerate(coordinates):
        for coordinate in coordinates[index:]:
            x_distance = coordinate.x - galaxy.x
            y_distance = coordinate.y - galaxy.y
            total_distance = total_distance + abs(x_distance) + abs(y_distance)
    return total_distance



def parse_space(filepath="./inputs/day11.txt"):

    with open(filepath, 'r') as f:
        line = f.readline().strip()
        initial_space = []
        while line:
            row = []
            row.extend(line)
            initial_space.append(row)
            line = f.readline().strip()

    space = expand_space(initial_space)

    return space







def part_one(filepath="./inputs/day11.txt"):

    expanded_space = parse_space(filepath)
    galaxies = get_coordinates(expanded_space)
    total_distance = compute_total_distance(galaxies)

    return total_distance



