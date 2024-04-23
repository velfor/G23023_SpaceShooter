import pygame
import sys
from settings import *
from player import Player
from player import Laser
from meteor_manager import MeteorManager
from text_obj import Text_Obj
from bg import Background
from bonus import Bonus
from bonus_manager import BonusManager
from shield import Shield

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SC_WIDTH, SC_HEIGHT))
        self.clock = pygame.time.Clock()
        self.run = True
        self.player = Player()
        self.meteor_manager = MeteorManager()
        self.text_hp = Text_Obj(500, 10, self.player.get_hp())
        self.game_over_bg = Background(GAME_OVER_FILENAME)
        self.score = 0
        self.text_score = Text_Obj(10, 10, self.score)
        self.bonus_manager = BonusManager()
        self.shield = Shield()
                
    def play(self):
        while self.run:
            self.check_events()
            self.update()
            self.check_collisions()
            self.draw()
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()

    def check_events(self):
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update(self):
        self.player.update()
        self.meteor_manager.update()
        self.text_hp.update(self.player.get_hp())
        self.text_score.update(self.score)
        self.bonus_manager.update()
        self.shield.update(self.player.get_center())
        if self.player.get_hp() == 0:
            self.game_over()
 
    def check_collisions(self):
        # игрок-метеоры
        for meteor in self.meteor_manager.meteors:
            if self.player.rect.colliderect(meteor.rect):
                self.player.reduce_hp(meteor.get_damage())
                meteor.random_position()
        # пули - метеоры
        for meteor in self.meteor_manager.meteors:
            for laser in self.player.laser_sprites:
                if meteor.rect.colliderect(laser.rect):
                    self.bonus_manager.generate_bonus(meteor)
                    meteor.random_position()
                    self.player.laser_sprites.remove(laser)
                    self.score += meteor.get_score()
        # игрок-бонусы
        for bonus in self.bonus_manager.bonuses:
            if self.player.rect.colliderect(bonus.rect):
                if bonus.get_type() == "shield":
                    self.shield.set_active()
                if bonus.get_type() == "pill":
                   self.player.add_hp(PILL_HP)
                if bonus.get_type() == "bolt":
                    self.player.set_three_lasers_active()
                self.bonus_manager.bonuses.remove(bonus)
        # щит - метеоры
        for meteor in self.meteor_manager.meteors:
            if self.shield.rect.colliderect(meteor.rect):
                meteor.random_position()
                
    def draw(self):
        self.screen.fill(BLACK)
        self.player.draw(self.screen)
        self.meteor_manager.draw(self.screen)
        self.text_hp.draw(self.screen)
        self.text_score.draw(self.screen)
        self.bonus_manager.draw(self.screen)
        self.shield.draw(self.screen)
        pygame.display.update()

    def game_over(self):
        while True:
            self.check_events()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                self.run = False
                break
            self.screen.fill(BLACK)
            self.game_over_bg.draw(self.screen)
            pygame.display.update()
        
           
        




    
