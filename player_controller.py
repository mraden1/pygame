import pygame as pg
from player_model import Player

class PlayerController:
  def __init__(self, game):
    super().__init__()
    self.game = game
    self.player = Player(200, 313, 64, 64, self) 
    self.player.set_character('Run_samurai.png', 8)

  def update(self, win):
    self.player.draw(win)