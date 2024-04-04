import pygame as pg

class EndScreen:
  def __init__(self, game):
    self.game = game
    self.scoreboard = game.scoreboard

  def endScreen(self):
    global pause, score, speed, obstacles
    pause = 0
    speed = 30
    obstacles = []

    run = True
    while run:
      pg.time.delay(100)
      for event in  pg.event.get():
        if event.type ==  pg.QUIT:
          run = False
          pg.quit()
        if event.type == pg.MOUSEBUTTONDOWN:
          run = False
          runner.falling = False
          runner.sliding = False
          runner.jumpin = False

      win.blit(bg, (0,0))
      largeFont =  pg.font.SysFont('comicsans', 80)
      lastScore = largeFont.render('Best Score: ' + str(updateFile()),1,(255,255,255))
      currentScore = largeFont.render('Score: '+ str(score),1,(255,255,255))
      win.blit(lastScore, (W/2 - lastScore.get_width()/2,150))
      win.blit(currentScore, (W/2 - currentScore.get_width()/2, 240))
      pg.display.flip()
    score = 0