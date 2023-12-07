import re
from collections import namedtuple


def get_points(card_numbers, winning_numbers):
    points = 0
    for number in card_numbers:
        if number in winning_numbers:
            if not points:
                points = 1
            else:
                points *= 2
    return points


def part_one(filepath="./inputs/day04.txt"):
    total_points = 0
    with open(filepath, 'r') as f:
        line = f.readline().strip()
        while line:
            winning_numbers = re.findall('[0-9]+', line.split("|")[0].split(":")[1])
            card_numbers = re.findall('[0-9]+', line.split("|")[1])
            total_points += get_points(card_numbers, winning_numbers)

            line = f.readline().strip()
    return(total_points)


def get_matches(card_numbers, winning_numbers):
    matches = 0
    for number in card_numbers:
        if number in winning_numbers:
            matches += 1
    return matches



def get_total_cards(cards):
    total = 0
    for index, card in enumerate(cards):
        total += 1
        for i in range(1, card +1):
            total += get_total_copies(cards, index + i)
    return total

def get_total_copies(cards, index):
    total = 1
    matches = cards[index]
    for i in range(1, matches + 1):
        total += get_total_copies(cards, index + i)
    return total



def part_two(filepath="./inputs/day04.txt"):
    cards = []
    with open(filepath, 'r') as f:
        line = f.readline().strip()
        while line:
            card_id = re.findall('[0-9]+', line.split("|")[0].split(":")[0])
            winning_numbers = re.findall('[0-9]+', line.split("|")[0].split(":")[1])
            card_numbers = re.findall('[0-9]+', line.split("|")[1])
            cards.append(get_matches(card_numbers, winning_numbers))
            line = f.readline().strip()

    return get_total_cards(cards)