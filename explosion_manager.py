import pygame
from settings import *
from explosion import Explosion
from meteor import Meteor

class ExplosionManager:
    def __init__(self):
        self.big_images=[]
        self.small_images=[]
        for i in range(9):
            self.big_images.append(pygame.image.
                load(EXPLOSION_FILENAME_PREFIX + str(i) +
                     EXPLOSION_FILENAME_POSTFIX).convert_alpha())
        for i in range(9):
            image = self.big_images[i]
            width = image.get_width()
            height = image.get_height()
            new_image = pygame.transform.scale(image, (width//2,height//2))
            self.small_images.append(new_image)
        self.explosions = []
        
    def generate_explosion(self, meteor):
        if meteor.get_anim_size() == "big":
            explosion = Explosion(meteor.get_center(), self.big_images)
            self.explosions.append(explosion)
        else:
            explosion = Explosion(meteor.get_center(), self.small_images)
            self.explosions.append(explosion)
            
    def update(self):
        for explosion in self.explosions:
            explosion.update()
            if explosion.get_inactive():
                self.explosions.remove(explosion)

    def draw(self, screen):
        for explosion in self.explosions:
            explosion.draw(screen)
                
