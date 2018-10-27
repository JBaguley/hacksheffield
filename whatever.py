import pygame
import time

"""returns number of backspaces used"""
def backspaces():
    stop = False
    count_BACKSPACE = 0
    position = 0
    while not stop:
        pressed = pygame.key.get_pressed()
        if pygame.key.get_pressed():
                position += 1
        if pressed[pygame.K_BACKSPACE]:
            count_BACKSPACE += 1
        if pressed[pygame.K_RETURN]:
            stop = True
    return [count_BACKSPACE, position]

def capitals():
    stop = False
    pressed = pygame.key.get_pressed()
    count_CAPS = 0
    count_LSHIFT = 0
    count_RSHIFT = 0
    count_BACKSPACE = 0
    while not stop:
        if pressed[pygame.K_LSHIFT]:
            count_LSHIFT += 1
        if pressed[pygame.K_RSHIFT]:
            count_RSHIFT += 1
        if pressed[pygame.K_CAPS]:
            count_CAPS += 1
        if pressed[pygame.K_BACKSPACE]:
            count_BACKSPACE += 1
        if pressed[pygame.K_RETURN]:
            stop = True
    return [count_CAPS, count_LSHIFT, count_RSHIFT]