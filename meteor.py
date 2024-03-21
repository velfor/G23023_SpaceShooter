import pygame
from settings import *
from random import randint

class Meteor(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedx = randint(-2,2)
        self.speedy = randint(2,6)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

    def draw(self,screen):
        screen.blit(self.image, self.rect)
        
