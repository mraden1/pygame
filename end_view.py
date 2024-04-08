import pygame as pg

class EndScreen:
  def __init__(self, game):
    self.game = game
    self.scoreboard = game.scoreboard

  def endScreen(self, score, win, W, H):
    run = True
    while run:
      pg.time.delay(100)
      win.blit(bg, (0,0))
      large_font =  pg.font.SysFont('comicsans', 80)
      last_score = large_font.render('Best Score: ' + str(updateFile()),1,(255,255,255))
      current_score = large_font.render('Score: '+ str(score),1,(255,255,255))
      win.blit(last_score, (W/2 - last_score.get_width()/2,150))
      win.blit(current_score, (W/2 - currentScore.get_width()/2, 240))
      play_again = large_font.render('Play Again?', 1, (255,255,255))
      play_again_rect = play_again.get_rect()
      win.blit(play_again, (W/2 - play_again.get_width()/2,150))
      pg.display.flip()

      for event in  pg.event.get():
        if event.type == pg.QUIT:
          run = False
          pg.quit()
        if event.type == pg.MOUSEBUTTONDOWN:
          self.game.player.falling = False
          self.game.player.sliding = False
          self.game.player.jumping = False
          if play_again_rect.collidepoint(event.pos):
            self.game.reset()

    score = 0