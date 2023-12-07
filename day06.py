from collections import namedtuple

Game = namedtuple('Game', ['time', 'record_distance'])


def ways_to_beat_record(game: Game) -> int:
    for hold_button_duration in range(0, game.time):
        time_left = game.time - hold_button_duration
        distance = hold_button_duration * time_left
        if distance > game.record_distance:
            print(hold_button_duration)
            break
    print(hold_button_duration)
    print(time_left)
    print(distance)
    return game.time - hold_button_duration - hold_button_duration + 1


def part_two_test() -> int:
    game = Game(71530, 940200)
    return ways_to_beat_record(game)

def part_two() -> int:
    game = Game(44899691, 277113618901768)
    return ways_to_beat_record(game)