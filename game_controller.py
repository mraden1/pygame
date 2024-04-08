import pygame as pg
from pygame.locals import *
from game_model import GameModel
from score_model import Scoreboard
from player_controller import PlayerController
from sound_controller import SoundController
from end_view import EndScreen
from obstacle_model import Saw
from start_controller import Start

import os
import random

class Game:
  def __init__(self):
    pg.init()
    self.player_controller = PlayerController(self)
    self.scoreboard = Scoreboard(self)
    self.game_model = GameModel(self)
    self.sound = SoundController(self)
    self.start_controller = Start(self)
    self.end_screen = EndScreen(self)
    self.obstacles = []
    self.run = False

    self.start_controller.running()

  def play(self):
    self.run = True
    while self.run:
      for event in pg.event.get():
        if event.type == USEREVENT+1:
          self.game_model.speed += 1
        elif event.type == USEREVENT+2:
          self.obstacles.append(self.game_model.create_obstacle(Saw(810, 310, 64, 64, self))) #Spike(810, 0, 48, 310, self)))
        self.game_model.check_events(self, event)
        for obstacle in self.obstacles:
          self.game_model.check_collision(self.player_controller.player, obstacle)
      self.game_model.update_window(self)


def main():
  G = Game()

if __name__ == "__main__":
  main()