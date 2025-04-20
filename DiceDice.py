from tkinter import *
from random import randint


def make_dice(side):

    def inner():
        return randint(1, side)

    return inner


dice = make_dice(6)

#####
class t:
    pass
class run:
    def __init__(self, dice):
        window = Tk()
        window.title("DiceDice!")
        window.geometry("960x540")
        player = [0, 1]
        scores = [0, 0]
        hint = Label(window,
                     text="Please type in the roll num",
                     relief="groove",
                     font=("bold"))
        icon = Label(window, bitmap="hourglass", compound="bottom")
        hint.pack()
        icon.pack()
    def show(self):

    def shift(person):
        return 1 - person

    def sum_digit(this, score):
        if score < 10:
            return score
        return score % 10 + this.sum_digit(score // 10)

    def take_turn(this, score, op_score, roll_time):
        if roll_time > 10 or roll_time < 0 or type(roll_time) != int:
            return 0, 0, False
        if roll_time == 0:
            total = this.sum_digit(op_score)
            roll_num = [total]
        else:
            roll_num = [dice() for _ in range(roll_time)]
            if min(roll_num) == 1:
                total = 1
            else:
                total = sum(roll_num)
        return total, roll_num, True

    def extra_turn(this, score, op_score):
        if op_score - score > 10:
            return True
        if this.gcd_10(score, op_score):
            return True
        return False

    def gcd_10(x, y):
        Max, Min = max(x, y), min(x, y)
        gcd = 1
        for i in range(Min, Max):
            if Min % i == 0 and Max % i == 0:
                gcd = i
        if gcd >= 10:
            return True
        return False


Run = run(dice)
