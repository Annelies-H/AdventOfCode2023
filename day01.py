



def get_first_digit(line: str) -> str:
    for char in line:
        if char.isdigit():
            return char
    raise Exception("No digit found: " + line)


def get_last_digit(line: str) -> str:
    for i in range(1, len(line) + 1):
        char = line[-i]
        if char.isdigit():
            return char
        i += 1
    raise Exception("No digit found")


def part_one(filepath="./inputs/day01.txt"):
    result = 0
    with open(filepath, 'r') as f:
        line = f.readline()
        while line:
            first_digit = get_first_digit(line)
            last_digit = get_last_digit(line)
            result += int(first_digit + last_digit)
            line = f.readline()
    return result

NUMBERS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
}

def get_first_number(line: str) -> str:
    numbers = []
    for number in NUMBERS.keys():
        index = line.find(number)
        if not index == -1:
            numbers.insert(index, number)
    return NUMBERS[numbers[0]]

def get_indexed_numbers(line: str) -> list():
    numbers = {}
    for number in NUMBERS.keys():
        index = line.find(number)
        if not index == -1:
            numbers[index] = NUMBERS[number]
            # repeat to get last ocurence as well
            rindex = line.rfind(number)
            if not rindex == -1:
                numbers[rindex] = NUMBERS[number]
    return sorted(numbers.items())


def part_two(filepath="./inputs/day01.txt"):
    result = 0
    with open(filepath, 'r') as f:
        line = f.readline()
        while line:
            numbers = get_indexed_numbers(line)
            first_digit = numbers[0][1]
            last_digit = numbers[-1][1]
            result += int(first_digit + last_digit)
            line = f.readline()
    return result