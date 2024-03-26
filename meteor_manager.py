import pygame
from settings import *
from meteor import Meteor
from random import randint

class MeteorManager:
    def __init__(self):
        filename_list = ["meteorBrown_big1.png", "meteorBrown_big2.png",
                        "meteorBrown_big3.png", "meteorBrown_big4.png",
                        "meteorBrown_med1.png", "meteorBrown_med3.png",
                        "meteorBrown_small1.png","meteorBrown_small2.png",
                        "meteorBrown_tiny1.png", "meteorBrown_tiny2.png"]
        self.meteors = []
        for filename in filename_list:
            x = randint(0, SC_WIDTH)
            y = randint(-SC_HEIGHT, 0)
            meteor = Meteor(x, y, "images\\meteors\\" + filename)
            if filename.find("big") > 0:
                meteor.set_damage(50)
            elif filename.find("med") > 0:
                meteor.set_damage(30)
            elif filename.find("small") > 0:
                meteor.set_damage(15)
            elif filename.find("tiny") > 0:
                meteor.set_damage(5)
            self.meteors.append(meteor)

    def update(self):
        for meteor in self.meteors:
            meteor.update()
            if meteor.rect.right <= 0 or meteor.rect.left >= SC_WIDTH \
            or meteor.rect.top >= SC_HEIGHT:
                meteor.rect.x = randint(0, SC_WIDTH)
                meteor.rect.y = randint(-SC_HEIGHT, 0)
                meteor.speedx = randint(-2,2)
                meteor.speedy = randint(2,6)

    def draw(self, screen):
        for meteor in self.meteors:
            meteor.draw(screen)
                
