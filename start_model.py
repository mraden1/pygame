import pygame as pg
from start_view import StartScreen

class StartModel:
  start_rect = None
  exit_rect = None
  def __init__(self, start, game):
    self.start = start
    self.game = game
    self.game_model = game.game_model

    self.font = pg.font.Font('freesansbold.ttf', 64)

  def create_title(self):
    title = self.font.render("Mildark's Adventure", True, (255, 255, 255))
    title_rect = title.get_rect()
    title_rect.center = (self.game_model.WIDTH / 2, self.game_model.HEIGHT / 4)
    return (title, title_rect, title_rect.center)

  def start_game(self):
    start = self.font.render('Start', True, (255, 255, 255))
    start_rect = start.get_rect()
    self.start_rect = start_rect
    start_rect.center = (self.game_model.WIDTH / 2, self.game_model.HEIGHT / 2)
    return (start, start_rect, start_rect.center)

  def exit_game(self):
    exit = self.font.render('Exit', True, (255, 255, 255))
    exit_rect = exit.get_rect()
    self.exit_rect = exit_rect
    exit_rect.center = (self.game_model.WIDTH / 2, self.game_model.HEIGHT / 2 + 100)
    return (exit, exit_rect, exit_rect.center)

  def handle_events(self, event):
    if event.type == pg.MOUSEBUTTONDOWN:
      if self.start_rect.collidepoint(event.pos):
        self.start.run = False
        self.game.play()
      if self.exit_rect.collidepoint(event.pos):
        self.start.run = False
        pg.quit()