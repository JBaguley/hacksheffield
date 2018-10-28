import pygame, time

back = "Backspace"
enter = "Enter"
shift = "Shift"
caps = "CapsLock"




#-------------- count ----------------------
def count(keyPresses):
    count_CAPS = 0
    count_SHIFT = 0
    count_BACKSPACE = 0
    t1 = keyPresses[0][1]

    for i in keyPresses:
        if i[0] == back:
            count_BACKSPACE += 1
        elif i[0] == caps:
            count_CAPS += 1
        elif i[0] == shift:
            count_SHIFT += 1
        elif i[0] == enter:
            t2 = i[1]

    return [count_CAPS, count_SHIFT, count_BACKSPACE, t2-t1]






#---------- speed between specific keys -----------------
def keySpeed(keyPresses):
    keys = {}
    t1 = 0
    k1 = keyPresses[0][0]

    # find dictionary of keypress times
    for i in keyPresses:
        k2 = i[0]
        t2 = i[1]
        if t1 != 0:
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
                keys[k1] = {k2: [t2-t1]}

        # first key
        # save key
        k1 = k2

        # restart timer
        t1 = t2

    # find averages
    total = 0
    totalNum = len(keys)-1
    print(keys)
    for i in keys:
        for j in keys[i]:
            l = len(keys[i][j])
            totalk = 0
            for k in keys[i][j]:
                totalk += k
            total += totalk
            keys[i][j] = totalk/l
    totalAverage = total/totalNum

    return [totalAverage, keys]






def main(keyPresses):
    Result = {}
    Result["avgKP"]   = keySpeed(keyPresses)[0]
    Result["specKP"]  = keySpeed(keyPresses)[1]
    Result["totTime"] = count(keyPresses)[3]
    Result["backs"]   = count(keyPresses)[2]
    Result["shifts"]  = count(keyPresses)[1]
    Result["caps"]    = count(keyPresses)[0]

    return Result





