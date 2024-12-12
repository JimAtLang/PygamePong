import pygame
from Ball import Ball
from pygame.locals import *


pygame.init()
screen = pygame.display.set_mode((400,400))
pygame.display.set_caption("Pong")
ball = Ball(50,100, 2, 3)
clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            quit()

    screen.fill((0,0,0))
    ball.update()
    if ball.rect.left < 0 or ball.rect.right > screen.get_width():
        ball.vx = -ball.vx
    if ball.rect.top < 0 or ball.rect.bottom > screen.get_height():
        ball.vy = - ball.vy
    screen.blit(ball.image, ball.rect)
    pygame.display.flip()
    clock.tick(60)
