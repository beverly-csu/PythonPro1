KEY_SWITCH_CAMERA = 'c'
KEY_SWITCH_MODE = 'z'

KEY_FORWARD = 'w'
KEY_BACK = 's'
KEY_LEFT = 'a'
KEY_RIGHT = 'd'

KEY_UP = 'e'
KEY_DOWN = 'q'

KEY_TURN_LEFT = 'n'
KEY_TURN_RIGHT = 'm'

KEY_BUILD = 'b'
KEY_DESTROY = 'v'


class Hero:
    def __init__(self, position, land):
        self.land = land
        self.mode = True
        self.hero = loader.loadModel('smiley')
        self.hero.setColor(1, 0.5, 0)
        self.hero.setScale(0.3)
        self.hero.reparentTo(render)
        self.hero.setPos(position)
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
        base.mouseInterfaceNode.setPos(-pos[0], -pos[1], -pos[2]-3)
        base.camera.reparentTo(render)
        base.enableMouse()
        self.cameraOn = False

    def changeView(self):
        if self.cameraOn:
            self.cameraUp()
        else:
            self.cameraBind()

    def turn_left(self):
        self.hero.setH((self.hero.getH() + 5) % 360)

    def turn_right(self):
        self.hero.setH((self.hero.getH() - 5) % 360)

    def check_dir(self, angle):
        if angle >= 0 and angle <= 20:
            return (0, -1)
        elif angle <= 65:
            return (1, -1)
        elif angle <= 110:
            return (1, 0)
        elif angle <= 155:
            return (1, 1)
        elif angle <= 200:
            return (0, 1)
        elif angle <= 245:
            return (-1, 1)
        elif angle <= 290:
            return (-1, 0)
        elif angle <= 335:
            return (-1, -1)
        else:
            return (0, -1)

    def look_at(self, angle):
        x_from = round(self.hero.getX())
        y_from = round(self.hero.getY())
        z_from = round(self.hero.getZ())

        dx, dy = self.check_dir(angle)
        x_to = x_from + dx
        y_to = y_from + dy
        return (x_to, y_to, z_from)

    def just_move(self, angle):
        pos = self.look_at(angle)
        self.hero.setPos(pos)

    def move_to(self, angle):
        if self.mode:
            self.just_move(angle)
        else:
            self.try_move(angle)
    
    def try_move(self, angle):
        pos = self.look_at(angle)
        if self.land.isEmpty(pos):
            pos = self.land.findHighestEmpty(pos)
            self.hero.setPos(pos)
        else:
            pos = (pos[0], pos[1], pos[2] + 1)
            if self.land.isEmpty(pos):
                self.hero.setPos(pos)


    def forward(self):
        angle = (self.hero.getH()) % 360
        self.move_to(angle)

    def back(self):
        angle = (self.hero.getH() + 180) % 360
        self.move_to(angle)
    
    def left(self):
        angle = (self.hero.getH() + 90) % 360
        self.move_to(angle)
    
    def right(self):
        angle = (self.hero.getH() + 270) % 360
        self.move_to(angle)

    def up(self):
        if self.mode:
            self.hero.setZ(self.hero.getZ() +  1)

    def down(self):
        if self.mode and self.hero.getZ() > 1:
            self.hero.setZ(self.hero.getZ() - 1)

    def accept_events(self):
        base.accept(KEY_TURN_LEFT, self.turn_left)
        base.accept(KEY_TURN_LEFT + '-repeat', self.turn_left)
        base.accept(KEY_TURN_RIGHT, self.turn_right)
        base.accept(KEY_TURN_RIGHT + '-repeat', self.turn_right)

        base.accept(KEY_UP, self.up)
        base.accept(KEY_UP + '-repeat', self.up)
        base.accept(KEY_DOWN, self.down)
        base.accept(KEY_DOWN + '-repeat', self.down)

        base.accept(KEY_FORWARD, self.forward)
        base.accept(KEY_FORWARD + '-repeat', self.forward)
        base.accept(KEY_BACK, self.back)
        base.accept(KEY_BACK + '-repeat', self.back)
        base.accept(KEY_LEFT, self.left)
        base.accept(KEY_LEFT + '-repeat', self.left)
        base.accept(KEY_RIGHT, self.right)
        base.accept(KEY_RIGHT + '-repeat', self.right)

        base.accept(KEY_SWITCH_CAMERA, self.changeView)
