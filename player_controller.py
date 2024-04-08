import pygame as pg
from player_model import Player

class PlayerController:
  def __init__(self, game):
    super().__init__()
    self.game = game
    self.player = Player(200, 240, 64, 64, self)

    run = {'images': 'run_samurai.png', 'frames': 8}
    jump = {'images': 'jump_samurai.png', 'frames': 9}
    walk = {'images': 'walk_samurai.png', 'frames': 8}
    idle = {'images': 'idle_samurai.png', 'frames': 9}
    collection = [run, jump, walk, idle]

    attack = {'attack1': {'images': 'attack_1.png', 'frames': 5},
              'attack2': {'images': 'attack_2.png', 'frames': 5},
              'attack3': {'images': 'attack_3.png', 'frames': 6}}
    
    self.player.set_character(collection, attack)

  def update(self, win):
    if self.game.game_model.speed > 60 and self.player.walking:
      self.player.walking = False
      self.player.running = True
    if self.player.attacking:
      self.player.draw(win)
    else:
      self.player.draw(win)