from direct.showbase.ShowBase import ShowBase
from mapmanager import MapManager
from hero import Hero

from time import time

class Game(ShowBase):
    def __init__(self):
        super().__init__()
        self.land = MapManager()
        self.land.loadLand('land.txt')
        self.hero = Hero((2, 2, 3), self.land)
        base.camLens.setFov(90)

        self.start = time()
        base.win.setCloseRequestEvent('exit_stage')
        base.accept('exit_stage', self.game_end)

    def game_end(self):
        end = time()
        print('Вы играли:', round((end-self.start) / 60, 2))
        base.destroy()
        exit()


game = Game()
game.run()