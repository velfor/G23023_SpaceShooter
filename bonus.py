import pygame
from settings import *
from random import randint

class Bonus(pygame.sprite.Sprite):
    def __init__(self, center, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images\\" + filename).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speed = BONUS_SPEED

    def update(self):
        self.rect.y += self.speed

    def draw(self,screen):
        screen.blit(self.image, self.rect)
