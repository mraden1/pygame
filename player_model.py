import pygame as pg
from pygame.locals import *
import os

class Player(object):
  run = [pg.image.load(os.path.join('pygame\images', f'{x}.png')) for x in range(8, 16)]
  jump = [pg.image.load(os.path.join('pygame\images', f'{x}.png')) for x in range(1, 8)]
  slide = [pg.image.load(os.path.join('pygame\images', 'S1.png'))] + [pg.image.load(os.path.join('pygame\images', 'S2.png'))]*7 + [pg.image.load(os.path.join('pygame\images', f'S{x}.png')) for x in range(3,6)]
  fall =  pg.image.load(os.path.join('pygame\images', '0.png'))
  jumpList = [1]*6 + [2]*12 + [3]*12 + [4]*12 + [0]*25 + [-1]*6 + [-2]*12 + [-3]*12 + [-4]*12

  def __init__(self, x, y, width, height, game):
    super().__init__()
    self.game = game
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.jumping = False
    self.sliding = False
    self.falling = False
    self.slideCount = 0
    self.jumpCount = 0
    self.runCount = 0
    self.slideUp = False

  def draw(self, win):
    if self.falling:
      win.blit(self.fall, (self.x, self.y + 30))
    elif self.jumping:
      self.y -= self.jumpList[self.jumpCount] * 1.3
      win.blit(self.jump[self.jumpCount//18], (self.x, self.y))
      self.jumpCount += 1
      if self.jumpCount > 108:
        self.jumpCount = 0
        self.jumping = False
        self.runCount = 0
      self.hitbox = (self.x+ 4, self.y, self.width-24, self.height-10)
    elif self.sliding or self.slideUp:
      if self.slideCount < 20:
        self.y += 1
        self.hitbox = (self.x+ 4, self.y, self.width-24, self.height-10)
      elif self.slideCount == 80:
        self.y -= 19
        self.sliding = False
        self.slideUp = True
      elif self.slideCount > 20 and self.slideCount < 80:
        self.hitbox = (self.x, self.y+3, self.width-8, self.height-35)

      elif self.slideCount >= 110:
        self.slideCount = 0
        self.runCount = 0
        self.slideUp = False
        self.hitbox = (self.x+ 4, self.y, self.width-24, self.height-10)
      win.blit(self.slide[self.slideCount//10], (self.x, self.y))
      self.slideCount += 1

    else:
      if self.runCount > 42:
        self.runCount = 0
      win.blit(self.run[self.runCount//6], (self.x,self.y))
      self.runCount += 1
      self.hitbox = (self.x+ 4, self.y, self.width-24, self.height-13)

      pg.draw.rect(win, (255,0,0),self.hitbox, 2)