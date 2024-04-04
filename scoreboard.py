import pygame as pg

class Scoreboard:
  def __init__(self, game):
    self.game = game
    self.score = 0

  def updateFile():
    f = open('scores.txt','r')
    file = f.readlines()
    last = int(file[0])

    if last < int(score):
        f.close()
        file = open('scores.txt', 'w')
        file.write(str(score))
        file.close()

        return score

    return last
