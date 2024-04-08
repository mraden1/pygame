import pygame as pg
from pygame.locals import *
import random
import os

class Player(pg.sprite.Sprite):
  jumpList = [1]*6 + [2]*12 + [3]*12 + [4]*12 + [0]*25 + [-1]*6 + [-2]*12 + [-3]*12 + [-4]*12

  def __init__(self, x, y, width, height, controller):
    super().__init__()
    self.controller = controller
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.walking = True
    self.running = False
    self.jumping = False
    self.attacking = False
    self.shootCount = 0
    self.jumpCount = 0
    self.runCount = 0
    self.walkCount = 0
    self.attackCount = 0
    self.hitbox = None

    self.local_actions = {'run': [],
                          'jump': [],
                          'walk': [], 
                          'idle': []}
    self.keys = list(self.local_actions.keys())
    self.attack = {}

  def set_character(self, collection=[], rec_attack={}):

    animation_frames = []
    x = 0
    for each in collection:
      full = pg.image.load(os.path.join('pygame/images', each['images']))
      frame_width = full.get_width() // each['frames']
      frame_height = full.get_height()

      for i in range(each['frames']):
        frame = full.subsurface(pg.Rect(i*frame_width, 0, frame_width, frame_height))
        animation_frames.append(frame)
      self.local_actions[self.keys[x]]= animation_frames.copy()
      x += 1
      animation_frames.clear()

    for x in range(1,4):
      attack = pg.image.load(os.path.join('pygame/images', rec_attack[f'attack{x}']['images']))
      frame_width = attack.get_width() // rec_attack[f'attack{x}']['frames']
      frame_height = attack.get_height()

      for i in range(rec_attack[f'attack{x}']['frames']):
        frame = attack.subsurface(pg.Rect(i*frame_width, 0, frame_width, frame_height))
        animation_frames.append(frame)
      self.attack[f'attack{x}'] = animation_frames.copy()
      animation_frames.clear()


  def draw(self, win, type=int):

    def jump_act(self, win):
      self.y -= self.jumpList[self.jumpCount] * 1.3
      self.hitbox = self.local_actions['jump'][self.jumpCount//18].get_rect()
      win.blit(self.local_actions['jump'][self.jumpCount//18], (self.x, self.y))
      self.jumpCount += 1
      if self.jumpCount > 108:
        self.jumpCount = 0
        self.jumping = False
        self.runCount = 0
      self.hitbox = pg.rect.Rect(self.x+(self.width//2), self.y+50, self.hitbox[2]//2, self.hitbox[3]//2)

      pg.draw.rect(win, (255,0,0), self.hitbox, 2)

    def walk_act(self, win):
      if self.walkCount > 42:
        self.walkCount = 0
      self.hitbox = self.local_actions['walk'][self.walkCount//6].get_rect()
      win.blit(self.local_actions['walk'][self.walkCount//6], (self.x, self.y))
      self.walkCount += 1
      self.hitbox = pg.rect.Rect(self.x+(self.width//2), self.y+50, self.hitbox[2]//2, self.hitbox[3]//2)

      pg.draw.rect(win, (255,0,0), self.hitbox, 2)

    def run_act(self, win):
      if self.runCount > 42:
        self.runCount = 0
      self.hitbox = self.local_actions['run'][self.runCount//6].get_rect()
      win.blit(self.local_actions['run'][self.runCount//6], (self.x,self.y))
      self.runCount += 1
      self.hitbox = pg.rect.Rect(self.x+(self.width//2), self.y+50, self.hitbox[2]//2, self.hitbox[3]//2)

      pg.draw.rect(win, (255,0,0), self.hitbox, 2)

    def attack(self, win, type=None):
      if self.attackCount > 4:
        self.walking = True
        self.attacking = False
        self.attackCount = 0
        return
      if self.attackCount == 1:
        self.controller.game.sound.samurai.play()
      self.hitbox = self.attack[f'attack{type}'][self.attackCount].get_rect()
      win.blit(self.attack[f'attack{type}'][self.attackCount], (self.x,self.y))
      self.attackCount += 1
      self.hitbox = pg.rect.Rect(self.x+(self.width//2), self.y+50, self.hitbox[2]//2, self.hitbox[3]//2)

      pg.draw.rect(win, (255,0,0), self.hitbox, 2)
    

    if self.jumping:
      jump_act(self, win)
    elif self.walking:
      walk_act(self, win)
    elif self.running:
      run_act(self, win)
    elif self.attacking:
      attack(self, win, random.randint(1,3))