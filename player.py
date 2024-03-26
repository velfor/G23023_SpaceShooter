import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(PLAYER_FILE_NAME).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = SC_WIDTH//2
        self.rect.bottom = SC_HEIGHT - 20
        self.hp = PLAYER_MAX_HP

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def get_hp(self):
        return self.hp

    def reduce_hp(self, damage):
        self.hp -= damage
