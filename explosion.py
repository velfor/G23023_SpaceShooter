import pygame
from settings import *

class Explosion(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.center = center
        images=[]
        for i in range(9):
            images.append(pygame.image.
                load(EXPLOSION_FILENAME_PREFIX + str(i) +
                     EXPLOSION_FILENAME_POSTFIX).convert_alpha())
        self.image = images[0]
        self.rect = self.image.get_rect()
        self.rect.center = self.center
        self.frame = 0
        self.delay = 100
        self.timer = pygame.time.get_ticks()
        self.is_active = True

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.timer > self.delay:
            self.frame += 1
            if self.frame < 9:
                self.image = images[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = self.center
                self.timer = now
            else:
                self.is_active = False

    def draw(self,screen):
        if self.is_active:
            screen.blit(self.image, self.rect)




            
