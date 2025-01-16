import pygame
from Ball import Ball
from Paddle import Paddle
from pygame.locals import *


pygame.init()
screen = pygame.display.set_mode((400,400))
pygame.display.set_caption("Pong")
ball = Ball(50,100, 2, 3)
paddle = Paddle(140, 360, 80, 10)
clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            quit()


    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        paddle.rect.x += 5
    if keys[pygame.K_LEFT]:
        paddle.rect.x -= 5
    screen.fill((0,0,0))
    ball.update()
    paddle.draw(screen)
    if ball.rect.left < 0 or ball.rect.right > screen.get_width():
        ball.vx = -ball.vx
    if ball.rect.top < 0 or ball.rect.bottom > screen.get_height():
        ball.vy = -ball.vy
    if pygame.Rect.colliderect(ball.rect, paddle.rect):
        ball.vy = -abs(ball.vy)
    screen.blit(ball.image, ball.rect)
    pygame.display.flip()
    clock.tick(60)
