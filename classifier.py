import main
from random import randint

user = main.load("joe")

percentage = 0
todo = []
wrong = [-1]
right = []
A = 1
B = 1
C = 1
D = 1
E = 1
THRESHOLD = 500

with open("data.txt", "r") as f:
    for line in f.readlines():
        pos = line.find(":")
        userdata = ""
        exec("userdata = "+line[pos+1:-1])
        todo.append([line[0:pos], main.data(userdata)])

while percentage < 70:
    wrong = []
    right = []
    for item in todo:
        score = user.checkTest(item[1], A, B, C, D, E)
        if (score>=THRESHOLD and item[0]=="joe") or (score<THRESHOLD and item[0]!="joe"):
            wrong.append(item)
        else: 
            right.append(item)

    A = randint(0,100)
    B = randint(0,100)
    C = randint(0,100)
    D = randint(0,100)
    E = randint(0,100)
    THRESHOLD = randint(0,10000)

    percentage = len(wrong)/(1.0*len(right))

    print(percentage)

    print(A, B, C, D, E)
        