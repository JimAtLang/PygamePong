import pygame.draw
from pygame.sprite import Sprite
from pygame.rect import Rect

RED = (255, 0, 0)

class Paddle(Sprite):
    def __init__(self, x, y, w, h):
        Sprite.__init__(self)
        self.rect = Rect(x, y, w, h)

    def draw(self, surface):
        pygame.draw.rect(surface, RED, self.rect)

