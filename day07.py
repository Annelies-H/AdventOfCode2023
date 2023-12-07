import re

CARD_STRENGTHS_MAPPING = {
    "T": "10",
    "J": "11",
    "Q": "12",
    "K": "13",
    "A": "14"
}

CARD_STRENGTHS_JOKERS_MAPPING = {
    "T": "10",
    "Q": "11",
    "K": "12",
    "A": "13",
    "J": "1",
}

HAND_TYPE_STRENGTH_MAPPING = {
    "five of a kind": 7,
    "four of a kind": 6,
    "full house": 5,
    "three of a kind": 4,
    "two pair": 3,
    "one pair": 2,
    "high card": 1,
}

def card_strength(card: str, jokers=False) -> int:
    if jokers:
        return int(CARD_STRENGTHS_JOKERS_MAPPING.get(card, card))
    return int(CARD_STRENGTHS_MAPPING.get(card, card))

def hand_strength(hand: str, jokers=False) -> int:
    if jokers:
        type = hand_type_jokers(hand)
    else:
        type = hand_type(hand)
    return HAND_TYPE_STRENGTH_MAPPING[type]

def hand_type(hand: str) -> int:
    cards = {}
    for card in hand:
        count = cards.get(card, 0)
        cards[card] = count + 1
    card_count = sorted(cards.values())
    if len(card_count) == 1:
        return "five of a kind"
    if len(card_count) == 5:
        return "high card"
    if 4 in card_count:
        return "four of a kind"
    if 3 in card_count:
        if 2 in card_count:
            return "full house"
        else:
            return "three of a kind"
    if len(card_count) == 3:
        return "two pair"
    if len(card_count) == 4:
        return "one pair"

def hand_type_jokers(hand: str) -> int:
    initial_type = hand_type(hand)
    jokers = len(re.findall('J', hand))
    if not jokers or jokers == 5:
        return initial_type
    if jokers == 4:
        return "five of a kind"
    if jokers == 3:
        if initial_type == "full house":
            return "five of a kind"
        return "four of a kind"
    if jokers == 2:
        if initial_type == "one pair":
            return "three of a kind"
        if initial_type == "two pair":
            return "four of a kind"
        if initial_type == "full house":
            return "five of a kind"
    if jokers == 1:
        if initial_type == "high card":
            return "one pair"
        if initial_type == "one pair":
            return "three of a kind"
        if initial_type == "two pair":
            return "full house"
        if initial_type == "three of a kind":
            return "four of a kind"
        if initial_type == "full house":
            return "four of a kind"
        if initial_type == "four of a kind":
            return "five of a kind"



def is_stronger(hand_1: str, hand_2, jokers=False) -> bool:
    hand_strength_1 = hand_strength(hand_1, jokers=jokers)
    hand_strength_2 = hand_strength(hand_2, jokers=jokers)
    if hand_strength_1 == hand_strength_2:
        for i in range(0, 5):
            card_strength_1 = card_strength(hand_1[i], jokers=jokers)
            card_strength_2 = card_strength(hand_2[i], jokers=jokers)
            if card_strength_1 != card_strength_2:
                return card_strength_1 > card_strength_2
    return hand_strength_1 > hand_strength_2

def sort_strongest(game: list[list[str]], jokers=False) -> list[list[str]]:
    if len(game) < 2:
        return game
    sorted_game = [game[0]]
    if is_stronger(hand_1=game[1][0], hand_2=game[0][0], jokers=jokers):
        sorted_game.append(game[1])
    else:
        sorted_game.insert(0, game[1])
    for handbid in game[2:]:
        hand = handbid[0]
        inserted = False
        for i in range(0, len(sorted_game)):
            if is_stronger(sorted_game[i][0], hand, jokers=True):
                sorted_game.insert(i, handbid)
                inserted = True
                break
        if not inserted:
            sorted_game.append(handbid)
    return sorted_game




def part_one(filepath="./inputs/day07.txt"):
    game = []
    with open(filepath, 'r') as f:
        line = f.readline()
        while line:
            game.append(line.strip().split(" "))
            line = f.readline()
    sorted_game = sort_strongest(game)
    result = 0
    for i in range(0, len(sorted_game)):
        result += int(sorted_game[i][1]) * (i+1)

    return(result)

def part_two(filepath="./inputs/day07.txt"):
    game = []
    with open(filepath, 'r') as f:
        line = f.readline()
        while line:
            game.append(line.strip().split(" "))
            line = f.readline()

    sorted_game = sort_strongest(game, jokers=True)
    result = 0
    for i in range(0, len(sorted_game)):
        result += int(sorted_game[i][1]) * (i+1)

    return(result)