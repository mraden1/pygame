import pygame as pg

class StartScreen:
  def __init__(self, game, start):
    self.controller = start
    self.game_model = game.game_model

    self.win, self.caption = self.game_model.create_view()
    self.bg, self.bgX, self.bgX2 = self.game_model.load_bg('bg.png')

  def draw(self, title={}, start_button={}, quit_button={}):
    self.win.blit(self.bg, (self.bgX, 0))
    self.win.blit(self.bg, (self.bgX2, 0))
    self.win.blit(title['text'], title['rect'])
    self.win.blit(start_button['text'], start_button['rect'])
    self.win.blit(quit_button['text'], quit_button['rect'])

  def update(self):
    pass

  