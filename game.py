import pygame
import sys
from settings import *
from player import Player
from meteor_manager import MeteorManager
from text_obj import Text_Obj

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SC_WIDTH, SC_HEIGHT))
        self.clock = pygame.time.Clock()
        self.run = True
        self.player = Player()
        self.meteor_manager = MeteorManager()
        self.text_hp = Text_Obj(500, 10, self.player.get_hp())
        
    def play(self):
        while self.run:
            self.check_events()
            self.update()
            self.check_collisions()
            self.draw()
            self.clock.tick(FPS)

    def check_events(self):
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update(self):
        self.player.update()
        self.meteor_manager.update()
        self.text_hp.update(self.player.get_hp())

    def check_collisions(self):
        pass

    def draw(self):
        self.screen.fill(BLACK)
        self.player.draw(self.screen)
        self.meteor_manager.draw(self.screen)
        self.text_hp.draw(self.screen)
        pygame.display.update()




    
