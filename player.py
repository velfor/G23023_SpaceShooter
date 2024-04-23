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
        self.laser_sprites = []
        self.fire_timer = pygame.time.get_ticks()
        self.speed = 0
        self.three_lasers_active = False
        self.three_lasers_timer = pygame.time.get_ticks()

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.speed = -PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            self.speed = PLAYER_SPEED
        self.rect.x += self.speed
        self.speed = 0

        self.fire()
        
        for laser in self.laser_sprites:
            laser.update()
            if laser.rect.bottom < 0:
                self.laser_sprites.remove(laser)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        for laser in self.laser_sprites:
            screen.blit(laser.image, laser.rect)

    def fire(self):
        now = pygame.time.get_ticks()
        if now - self.three_lasers_timer > THREE_LASER_RUNTIME:
            self.three_lasers_timer = now
            self.three_lasers_active = False
        keys = pygame.key.get_pressed()            
        if keys[pygame.K_SPACE] and now - self.fire_timer > FIRE_DELAY:
            self.fire_timer = now
            if self.three_lasers_active:
                laser = Laser(self.rect.centerx, self.rect.top)
                left_laser = Laser(self.rect.left + 10, self.rect.top + 40)
                right_laser = Laser(self.rect.right-10, self.rect.top + 40)
                self.laser_sprites.append(laser)
                self.laser_sprites.append(left_laser)
                self.laser_sprites.append(right_laser)
            else:
                laser = Laser(self.rect.centerx, self.rect.top)
                self.laser_sprites.append(laser)

    def get_hp(self):
        return self.hp

    def reduce_hp(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def add_hp(self, hp):
        self.hp += hp
        if self.hp > 100:
            self.hp = 100

    def get_centerx(self):
        return self.rect.centerx

    def get_center(self):
        return self.rect.center

    def get_top(self):
        return self.rect.top

    def set_three_lasers_active(self):
        self.three_lasers_active = True

class Laser(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(LASER_FILE_NAME).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedy = LASER_SPEEDY

    def update(self):
        self.rect.y -= self.speedy

    def draw(self, screen):
        screen.blit(self.image, self.rect)










