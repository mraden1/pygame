import pygame as pg
from pygame.locals import *
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
    self.jumpCount = 0
    self.runCount = 0
    self.walkCount = 0

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
      self.attack[f'attack{x}'] = animation_frames
      animation_frames.clear()


  def draw(self, win):

    def jump_act(self, win):
      self.y -= self.jumpList[self.jumpCount] * 1.3
      win.blit(self.local_actions['jump'][self.jumpCount//18], (self.x, self.y))
      self.jumpCount += 1
      if self.jumpCount > 108:
        self.jumpCount = 0
        self.jumping = False
        self.runCount = 0
      self.hitbox = (self.x+ 4, self.y, self.width-24, self.height-10)

    def walk_act(self, win):
      if self.walkCount > 42:
        self.walkCount = 0
      win.blit(self.local_actions['walk'][self.walkCount//6], (self.x, self.y))
      self.walkCount += 1
      self.hitbox = (self.x+4, self.y, self.width, self.height)

      pg.draw.rect(win, (255,0,0), self.hitbox, 2)

    def run_act(self, win):
      if self.runCount > 42:
        self.runCount = 0
      win.blit(self.self.local_actions['run'][self.runCount//6], (self.x,self.y))
      self.runCount += 1
      self.hitbox = (self.x+ 4, self.y, self.width-24, self.height-13)

      pg.draw.rect(win, (255,0,0),self.hitbox, 2)
    

    if self.jumping:
      jump_act(self, win)
    elif self.walking:
      walk_act(self, win)
    elif self.running:
      run_act(self, win)