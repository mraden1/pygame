import pygame
from pygame.locals import *
from settings import Settings
from scoreboard import Scoreboard
from end_screen import EndScreen
from obstacles import Saw, Spike
from start_screen import StartScreen
import os
import random

class Game():
  def __init__(self): 
    self.settings = Settings()
    self.player = Player(200, 313, 64, 64, self)
    self.run = False
    self.start_screen = StartScreen(self)

    self.obstacles = []

  def play(self):
    self.run = True
    while self.run:
      self.check_events()
      self.settings.update_window()

  def check_events(self):
    self.check_collision()

    for event in pg.event.get():
      if event.type == pg.QUIT:
        self.run = False
        pg.quit()
        quit()
      elif event.type == USEREVENT+1:
          self.increase_speed(self.settings.speed)
      elif event.type == USEREVENT+2:
        r = randint(0,1)
        if r == 0:
          self.obstacles.append(Saw(810, 310, 64, 64))
        else:
          self.obstacles.append(Spike(810, 0, 48, 310))

    if keys[pg.K_SPACE] or keys[pg.K_UP]:
      if not (self.player.jumping):
        self.player.jumping = True

    if keys[pg.K_DOWN]:
      if not (self.player.sliding):
        self.player.sliding = True

  def increase_speed(self, speed):
    speed += 1

  def check_collision(self, pause, fallspeed, speed):
    for obstacle in self.obstacles:
      if pg.rect(obstacle).collide(pg.rect(self.player.hitbox)):
        print('player hit')
