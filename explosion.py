import pygame
from settings import *

class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, images):
        pygame.sprite.Sprite.__init__(self)
        self.center = center
        self.images = images
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.center = self.center
        self.frame = 0
        self.delay = 50
        self.timer = pygame.time.get_ticks()
        self.is_active = True

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.timer > self.delay:
            self.frame += 1
            if self.frame < 9:
                self.image = self.images[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = self.center
                self.timer = now
            else:
                self.is_active = False

    def draw(self,screen):
        if self.is_active:
            screen.blit(self.image, self.rect)

    def get_inactive(self):
        return not self.is_active


            
