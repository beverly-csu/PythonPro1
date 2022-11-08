KEY_SWITCH_CAMERA = 'c'
KEY_SWITCH_MODE = 'z'

KEY_FORWARD = 'w'
KEY_BACK = 's'
KEY_LEFT = 'a'
KEY_RIGHT = 'd'

KEY_TURN_LEFT = 'n'
KEY_TURN_RIGHT = 'm'


class Hero:
    def __init__(self, position, land):
        self.land = land
        self.hero = loader.loadModel('smiley')
        self.hero.setColor(1, 0.5, 0)
        self.hero.setScale(0.3)
        self.hero.reparentTo(render)
        self.cameraBind()
        self.accept_events()

    def cameraBind(self):
        base.disableMouse()
        base.camera.setH(180)
        base.camera.reparentTo(self.hero)
        base.camera.setPos(0, 0, 1.5)
        self.cameraOn = True

    def cameraUp(self):
        pos = self.hero.getPos()
        base.mouseInterfaceMode.setPos(-pos[0], -pos[1], -pos[2]-3)
        base.camera.reparentTo(render)
        base.enableMouse()
        self.cameraOn = False

    def changeView(self):
        if self.cameraOn:
            self.cameraUp()
        else:
            self.cameraBind()

    def accept_events(self):
        base.accept(KEY_SWITCH_CAMERA, self.changeView)