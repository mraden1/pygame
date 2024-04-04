import pygame as pg
import os

class Saw(pg.sprite.Sprite):
 rotate = [ pg.image.load(os.path.join('pygame\images', f'SAW{x}.png')) for x in range(4)] 

 def __init__(self, x, y, width, height, game):
  super().__init__()
  self.game = game
  self.x = x
  self.y = y
  self.width = width
  self.height = height
  self.rotateCount = 0
  self.vel = 1.4

 def draw(self, win):
  self.hitbox = (self.x + 10, self.y + 5, self.width - 20, self.height - 5)
  pg.draw.rect(win, (255,0,0), self.hitbox, 2)
  if self.rotateCount >= 8:
   self.rotateCount = 0
  win.blit( pg.transform.scale(self.rotate[self.rotateCount//2], (64,64)), (self.x,self.y))
  self.rotateCount += 1


class Spike(Saw):
 img = pg.image.load(os.path.join('pygame\images', 'spike.png'))

 def __init__(self, x, y, width, height, game):
  super().__init__(x, y, width, height, game)

 def draw(self, win):
  self.hitbox = (self.x + 10, self.y, 28,315)
  pg.draw.rect(win, (255,0,0), self.hitbox, 2)
  win.blit(self.img, (self.x, self.y))