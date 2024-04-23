import pygame
from settings import *
from explosion import Explosion
from meteor import Meteor

class ExplosionManager:
    def __init__(self):
        self.images=[]
        for i in range(9):
            self.images.append(pygame.image.
                load(EXPLOSION_FILENAME_PREFIX + str(i) +
                     EXPLOSION_FILENAME_POSTFIX).convert_alpha())
        self.explosions = []
        
    def generate_explosion(self, meteor):
        explosion = Explosion(meteor.get_center(), self.images)
        self.explosions.append(explosion)
            
    def update(self):
        for explosion in self.explosions:
            explosion.update()
            if explosion.get_inactive():
                self.explosions.remove(explosion)

    def draw(self, screen):
        for explosion in self.explosions:
            explosion.draw(screen)
                
