import pygame as pg

class SoundController:
  def __init__(self, game):
    self.game = game
    pg.mixer.init()
    self.samurai = pg.mixer.Sound('pygame/sounds/sword_sound.mp3')
