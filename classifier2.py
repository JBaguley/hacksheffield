import numpy as np
import math


def check(username,data):
   #load in data
   [train, iteration, time] = loaddata(username)

   #calculate the feature matrix
   features = calcFeatures(train, iteration, time)

   #calcualte mv pairs
   meve = mvpair(features, iteration, time)

   #percentage of generate bool and return

   bools = generateBool(meve)

   ann = percentage(bools)

   if ann < 0.65:
       return False
   else:
       return True


def loaddata(username):
   train = np.genfromtxt(username + '.txt', delimiter=",")
   [iteration, time] = np.shape(train)

   return train, iteration, time


#train = np.genfromtxt('pword.txt', delimiter=",")
#[iteration, time] = np.shape(train)



def calcFeatures(train, iteration, time):
   features = np.zeros((iteration, time + 1))

   for i in range(iteration):
       features[i][time - 1] = train[i][-1]
       features[i][time] = round(train[i][-1] / time, 2)
       for j in range(0, time - 1):
           features[i][j] = train[i][j + 1] - train[i][j]

   return features



def calcMean(array, column, itteration, time):
   sum = 0
   for i in range(itteration):
       sum = sum + array[i][column]

   return round(sum / len(array), 2)


def calcMeanVar(array, column, itteration, time):
   mean = calcMean(array, column, itteration, time)
   sum = 0
   for i in range(itteration):
       sum = sum + (mean - array[i][column]) ** 2

   var = round((sum / len(array)), 2)

   return mean, var


def mvpair(array, itteration, time):
   mv = []
   for i in range(time + 1):
       mv.append(calcMeanVar(array, i, itteration, time))

   return mv

#print(mvpair(features))

input = [135, 90, 90, 500, 90, 90, 200, 75, 35, 90, 1000, 85]
print(input)




#meve = mvpair(features)


def generateBool(meve):
   accept = []
   for i in range(len(input)):
       sd = math.sqrt(meve[i][1])
       diff = abs(meve[i][0]-input[i])
       if diff<sd:
           accept.append(True)
       else:
           accept.append(False)

   return accept


def percentage(array):
   sum1 = 0
   for i in range(len(array)):
       if array[i]:
           sum1 = sum1 + 1
   return round(sum1 / len(array), 2)


