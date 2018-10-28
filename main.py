#hahaha its stu pickles
import pickle as stu

THRESHOLD = 1



class data:
    def __init__(self, values):
        self.avgKP = values["avgKP"]
        self.totTime = values["totTime"]
        self.back = values["back"]
        self.shifts = values["shifts"]
        self.caps = values["caps"]

    def check(self, user):
        score = 0

        score += abs(self.avgKP - user.avgKP)
        score += abs(self.totTime - user.totTime)
        score += abs(self.back - user.back)
        score += abs(self.shifts - user.shifts)
        score += abs(self.caps - user.caps)

        return score


def save(username, values):
    user = data(values)

    with open(username + ".txt") as f:
        stu.dump(f)

def check(username, values):

    user_check = data(values)

    with open(username+".txt") as f:
        user = stu.load(f)

    score = user_check.check(user)

    print(score)

    return score<THRESHOLD