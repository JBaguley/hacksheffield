import main
from random import randint

user = main.load("joe")

percentage = 0
todo = []
wrong = [-1]
false_pos = []
right = []
A = 1
B = 1
C = 1
D = 1
E = 1
correct_attempts = 0
THRESHOLD = 500

with open("data.txt", "r") as f:
    for line in f.readlines():
        pos = line.find(":")
        userdata = ""
        exec("userdata = "+line[pos+1:-1])
        todo.append([line[0:pos], main.data(userdata)])

while percentage < 70 or not false_pos:
    wrong = []
    right = []
    false_pos = []
    correct_attempts = 0
    for item in todo:
        score = user.checkTest(item[1], A, B, C, D, E)
        if (score>=THRESHOLD and item[0]=="joe"):
            correct_attempts += 1
            wrong.append(item)
        elif (score<THRESHOLD and item[0]!="joe"):
            false_pos.append(item)
            wrong.append(item)
        else: 
            right.append(item)

    A = randint(0,10)
    B = randint(0,10)
    C = randint(0,10)
    D = randint(0,10)
    E = randint(0,10)
    THRESHOLD = randint(000,1000)

    percentage = (len(right)/(1.0*len(todo)))*100

print(percentage)
print(correct_attempts)
print(A, B, C, D, E)
print(THRESHOLD)
        