import pygame as pg
import random
import os

class GameModel:
  def __init__(self, game):
    self.game = game
    self.player = game.player_controller
    self.WIDTH, self.HEIGHT = (800, 440)
    self.lives = 3
    
    self.clock = pg.time.Clock()

    self.win = self.create_view()[0]
    self.bg, self.bgX, self.bgX2 = self.load_bg('bg.png')

    pg.time.set_timer(pg.USEREVENT+1, 500)
    pg.time.set_timer(pg.USEREVENT+2, random.randint(4000, 6000))

    self.largeFont = pg.font.SysFont('comicsans', 30)
    self.text = self.largeFont.render('Score: ' + str(self.game.scoreboard.score), 1, (255,255,255))

    self.speed = 30

    self.pause = 0
    self.fallSpeed = 0

  def set_clock(self):
    self.clock.tick(self.speed)

  def create_view(self, width=800, height=440, in_cap='Side Scroller'):
    win = pg.display.set_mode((width,height))
    caption = pg.display.set_caption(in_cap)
    return (win, caption)

  def update_window(self, game=None):
    self.bg, self.bgX, self.bgX2, self.win = self.manage_bg(self.bg, self.bgX, self.bgX2, self.win)
    self.manage_obstacles(game.obstacles)
    self.set_clock()
    game.player_controller.update(self.win)
    self.win.blit(self.text, (700, 10))
    pg.display.flip()

  def manage_obstacles(self, obstacles=[]):
    for obstacle in obstacles:
      obstacle.x -= 1.4
      if obstacle.x == obstacle.width * -1:
        obstacle.pop(index(obstacle))
        obstacle.kill()
      else:
        obstacle.draw(self.win)

  def load_bg(self, background=None):
    bg = pg.image.load(os.path.join('pygame\images', background)).convert()
    bgX = 0
    bgX2 = bg.get_width()
    return (bg, bgX, bgX2)

  def check_collision(self, player, obstacle):
    if player.hitbox.colliderect(obstacle.hitbox):
      if player.attacking == True:
        print('obstacle killed')
        self.game.obstacles.pop(self.game.obstacles.index(obstacle))
        obstacle.kill()
        self.game.scoreboard.score += 100
      else:
        print('player hit')
        self.game.scoreboard.updateFile()
        self.game.scoreboard.score = 0
        if self.lives == 0:
          print('endscreen')
          self.game.run = False
          self.game.end_screen.end_screen(self.game.scoreboard.score, self.win, self.WIDTH, self.HEIGHT)
        else:
          self.lives -= 1
      return True
    return False

  def manage_bg(self, bg=None, bgX=None, bgX2=None, win=None):
    bgX -= 1.4
    bgX2 -= 1.4

    win.blit(bg, (bgX, 0))
    win.blit(bg, (bgX2,0))

    if bgX < bg.get_width() * -1:
      bgX = bg.get_width()
    if bgX2 < bg.get_width() * -1:
      bgX2 = bg.get_width()

    return (bg, bgX, bgX2, win)

  def create_obstacle(self, obstacle1=None):
      return(obstacle1)

  def check_events(self, game, event):
    if event.type == pg.QUIT:
      game.run = False
      pg.quit()
      quit()
    elif event.type == pg.KEYDOWN:
      if event.key == event.key == pg.K_UP:
        print('up or space pressed')
        if not (game.player_controller.player.jumping):
          game.player_controller.player.jumping = True

      elif event.key == pg.K_SPACE:
        print('down presses')
        if not (game.player_controller.player.attacking):
          game.player_controller.player.walking = False
          game.player_controller.player.running = False
          game.player_controller.player.attacking = True
        