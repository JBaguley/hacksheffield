import numpy as np
import random
import math

theTruth = [[0.46, 6.6, 12., 0.2], [0.78, 8.56, 0, 0.2],
            [1.2, 1, 9, 0.2], [6.5, 65, 4, 0.25], [3.5, 13.2, 0, 0.2, 4]]
print(theTruth)
train = np.genfromtxt('train.txt', delimiter=",")

[readin, features] = np.shape(train)
eta = 0.05
winit = 1
alpha = 0.9
users = 5

repetitions = 10

W = winit*np.random.rand(users, features-1)

for t in range(0,readin):
    x = train[t, :]                          # pick a training instance using the random index
    print(x)
    '''   h = W.dot(x)/users                    # get output firing
    h = h.reshape(h.shape[0],-1)            # reshape h into a numpy 2d array

    output = np.max(h)                   # get the max in the output firing vector + noise
    k = np.argmax(h)                     # get the index of the firing neuron

    counter[0,k] += 1                       # increment counter for winner neuron

    dw = eta * (x.T - W[k,:])               # calculate the change in weights for the k-th output neuron
                                            # get closer to the input (x - W)

    W[k,:] = W[k,:] + dw                    # weights for k-th output are updated

print(W)
'''

