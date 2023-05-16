# File created by Nathan Cutaran
import pygame as pg
from pygame.sprite import Sprite
from settings import *
from random import randint
vec = pg.math.Vector2

# creates a player class
class Bird(Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        # properties
        self.game = game
        self.image = pg.Surface((50,50))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.cofric = 0.1
        self.canjump = False

# method in player class that defines the inputs and what they do, when this key gets pressed the player acceleration does this...
    # def input(self):
    #     keystate = pg.key.get_pressed()
        
    #     if keystate[pg.K_a]:
    #         self.acc.x = -PLAYER_ACC
      
    #     if keystate[pg.K_d]:
    #         self.acc.x = PLAYER_ACC


# method in player class that contricts the player jump to the platform 
    def jump(self):
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        if hits:
            self.vel.y = -PLAYER_JUMP

# method in player class that defines the boundaries, in this case it wraps around
    def inbounds(self):
        if self.rect.x <= 0:
           self.pos.x = 0
        if self.rect.x >= 700:
            self.pos.x =  650




# method in the player class that is an output to the input, hence "update", it calles the methods self.input() and self.inbounds()
    def update(self):
        self.acc = vec(0, PLAYER_GRAV)
        self.acc.x = self.vel.x * PLAYER_FRICTION
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos
        self.inbounds()


# creates a new platform class
class Pipe(Sprite):
    def __init__(self, x, y, width, height, color, variant):
        Sprite.__init__(self)
        self.width = width
        self.height = height
        self.image = pg.Surface((self.width,self.height))
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.variant = variant
