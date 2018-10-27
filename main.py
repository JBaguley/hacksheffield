import pygame, time


#----------- total time ----------------
# returns: time taken to type in ticks
def speed():
    # check for first key pressed to start timer
    stop = False
    while not stop:
        for event in pygame.event.get():
            if event.key != pygame.K_RETURN:
                t = time.time()
                stop = True
            else:
                return 0

    # loop until enter is pressed
    stop = False
    while not stop:
    for event in pygame.event.get():
        # change if want a different key to end typing
        if event.key == pygame.K_RETURN:
            stop = True
            return time.time() - t





#---------- speed between specific keys -----------------
def speedSpecKeys():
    first = True
    keys = {}
    while not stop:
        for event in pygame.event.get() :
            if event.key == pygame.K_RETURN:
                stop = True
                if first:
                    return keys
                else:
                    return
            if event.type == pygame.keydown:
                t2 = time.time()
                k2 = pygame.key.name(event.key)

                # not first key
                # add k1 -> k2 to dictionary
                if not first:
                    # if k1 in first key
                    if k1 in keys:
                        # if k2 is in second key after k1
                        if k2 in keys[k1]:
                            keys[k1][k2].append(t2-t1)
                        # k1 not in second key after k1
                        else:
                            keys[k1][k2] = [t2-t1]
                    # if k1 not in first key
                    else:
                        keys[k1] = {k2 : [t2-t1]}

                # first key
                # save key
                else:
                    first = False
                    k1 = k2

                # restart timer
                t1 = time.time()

def main(keyPresses):
    Result = {}
    Result["avgKP"]   = averageKeySpeed()
    Result["specKP"]  = speedSpecKeys()
    Result["totTime"] = totTime()
    Result["backs"]   = backspaces()
    Result["shifts"]  = shifts()
    Result["caps"]    = capitals()













if __name__ == "__main__":
    print main()
