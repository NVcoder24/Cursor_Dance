from pynput.mouse import Button, Controller
from time import sleep
from random import choice
from threading import Thread

move = 2
mouse = Controller()
s = 0.05

def get_rand_pos():
    a = [True, False]
    return [choice(a), choice(a)]

def dance():
    while(True):
        pos = get_rand_pos()
        cpos = mouse.position

        pos1 = cpos[0]
        pos2 = cpos[1]

        if pos[0] == True:
            pos1 = pos1 + move
        elif pos[0] == False:
            pos1 = pos1 - move
        else:
            pass

        if pos[1] == True:
            pos2 = pos2 + move
        elif pos[1] == False:
            pos2 = pos2 - move
        else:
            pass

        mouse.position = (pos1, pos2)

        sleep(s)

dance()
