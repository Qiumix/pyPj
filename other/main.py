from random import randint


def make_dice(num):

    def inner():
        return randint(1, num)

    return inner


dice = make_dice(6)


def cls_make(is_cmd):
    """
    os库在git bash的情况下有点小问题，cmd会返回0，所以打印转义字符
    """

    def inner_0():
        from os import system
        if is_cmd:
            system("cls")
        else:
            system("clear")

    def inner():
        print('\033[2J\033[H', end='')

    return inner


cls = cls_make(False)


def roll(roll_time, player, another_player, dice=dice):
    assert type(roll_time) == int and\
          roll_time <= 10 and roll_time >= 0
    if roll_time == 0:

        def get_digit(score):
            if score < 10:
                return score
            return score % 10 + get_digit(score // 10)

        outcome = get_digit(another_player.score)
    else:
        outcome = [dice() for _ in range(roll_time)]
    print(f"The dice that you roll is:{outcome}")
    if min(outcome) == 1:
        get_score = 1
    else:
        get_score = sum(outcome)
    print(f"{player.name} Get {get_score} scores")
    player.score += get_score


def extra_turn(player, another_player):
    if another_player.score - player.score > 10:
        return True
    return False


class player:

    def __init__(self, num, score=0):
        self.num = num
        self.score = score


def shift(person):
    return 1 - person


Players = [player(0), player(1)]


def main(Players):
    person = 0
    while True:
        if person == 0:
            i = 0
            while i == 0 or extra_turn(Players[person],
                                       Players[shift(person)]):
                roll_times = int(input(f"Get player {person}'s roll time:\n"))
                roll(roll_times, )
