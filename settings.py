import pygame as pg
import random

class Settings:
  def __init__(self, game):
    pg.init()
    self.game = game
    self.player = game.player
    self.W, self.H = 800, 437
    self.win = pg.display.set_mode((self.W,self.H))
    self.caption = pg.display.set_caption('Side Scroller')

    self.bg = pg.image.load(os.path.join('images', 'bg.png')).convert()
    self.bgX = 0
    self.bgX2 = bg.get_width()

    self.clock = pg.time.Clock()

    self.largeFont = pg.font.SysFont('comicsans', 30)
    self.text = largeFont.render('Score: ' + str(score), 1, (255,255,255))

    pg.time.set_timer(USEREVENT+1, 500)
    pg.time.set_timer(USEREVENT+2, random.randint(4000, 6000))
    self.speed = 30

    self.pause = 0
    self.fallSpeed = 0

    def update_window(self):
      self.player.draw(self.win)
      self.manage_bg()
      self.manage_obstacles(self.game.obstacles)

      self.win.blit(self.text, (700, 10))
      pg.display.flip()

    def manage_obstacles(self, obstacles):
      for events in pg.event.get():
        if event.type == USEREVENT+1:
          self.speed += 1
        elif event.type == USEREVENT+2:
          r = randint(0,1)
          if r == 0:
            obstacles.append(Saw())
          else:
            obstacles.append(Spike())
      
      for obstacle in obstacles:
        obstacle.x -= 1.4
        if obstacle.x == obstacle.width * -1:
          obstacle.pop(index(obstacle))
          obstacle.kill()
        else:
          obstacle.draw(self.win)

    def manage_bg(self):
      self.bgX -= 1.4
      self.bgX2 -= 1.4

      self.win.blit(bg, (bgX, 0))
      self.win.blit(bg, (bgX2,0))

      if self.bgX < self.bg.get_width() * -1:
        self.bgX = self.bg.get_width()
      if self.bgX2 < self.bg.get_width() * -1:
        self.bgX2 = self.bg.get_width()