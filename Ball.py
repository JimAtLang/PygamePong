import pygame.display
from pygame.sprite import Sprite


class Ball(Sprite):
    def __init__(self, x, y , vx, vy):
        Sprite.__init__(self)
        self.image = pygame.image.load("images/ball.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vx = vx
        self.vy = vy

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy

