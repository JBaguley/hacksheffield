#hahaha its stu pickles
import pickle as stu

THRESHOLD = 537
A = 8
B = 1
C = 2
D = 1
E = 10



class data:
    def __init__(self, values):
        self.avgKP = values["avgKP"]
        self.totTime = values["totTime"]
        self.backs = values["backs"]
        self.shifts = values["shifts"]
        self.caps = values["caps"]

    def check(self, user):
        score = 0

        score += A*abs(self.avgKP - user.avgKP)
        score += B*abs(self.totTime - user.totTime)
        score += C*abs(self.backs - user.backs)
        score += D*abs(self.shifts - user.shifts)
        score += E*abs(self.caps - user.caps)

        return score

    def checkTest(self, user, A, B, C, D, E):
        score = 0

        score += A*abs(self.avgKP - user.avgKP)
        score += B*abs(self.totTime - user.totTime)
        score += C*abs(self.backs - user.backs)
        score += D*abs(self.shifts - user.shifts)
        score += E*abs(self.caps - user.caps)

        return score


def save(username, values):
    user = data(values)

    with open(username + ".txt", "wb") as f:
        stu.dump(user, f)

def load(username):
    with open(username + ".txt", "rb") as f:
        user = stu.load(f)

    return user

def check(username, values):

    user_check = data(values)

    with open(username+".txt", "rb") as f:
        user = stu.load(f)

    score = user_check.check(user)

    print(score)

    return score<THRESHOLD