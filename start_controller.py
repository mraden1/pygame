import pygame as pg
from start_view import StartScreen
from start_model import StartModel

class Start:
  def __init__(self, game):
    self.game = game
    self.start_view = StartScreen(self.game, self)
    self.model = StartModel(self, game)

    self.run = True
    self.main_loop()

  def main_loop(self):
    while self.run:
      for event in pg.event.get():
        self.model.handle_events(event)
      title, start, exit = {}, {}, {}
      attributes = self.model.create_title()
      title['text'] = attributes[0] 
      title['rect'] = attributes[1]
      attributes = self.model.start_game()
      start['text'] = attributes[0] 
      start['rect'] = attributes[1] 
      attributes = self.model.exit_game()
      exit['text'] = attributes[0]
      exit['rect'] = attributes[1] 
      self.start_view.draw(title, start, exit)
      self.start_view.update()
      pg.display.flip()