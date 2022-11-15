from direct.showbase.ShowBase import ShowBase
from mapmanager import MapManager
from hero import Hero


class Game(ShowBase):
    def __init__(self):
        super().__init__()
        self.land = MapManager()
        self.land.loadLand('land.txt')
        self.hero = Hero((2, 2, 3), self.land)
        base.camLens.setFov(90)

game = Game()
game.run()