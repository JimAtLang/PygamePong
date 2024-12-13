import pygame
from Ball import Ball
from pygame.locals import *


pygame.init()
screen = pygame.display.set_mode((400,400))


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            quit()
