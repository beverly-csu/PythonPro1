class MapManager():
    def __init__(self):
        self.model = 'block.egg'
        self.texture = 'block.png'
        self.colors = [(0.2, 0.2, 0.35, 1),
                       (0.2, 0.5, 0.2, 1),
                       (0.7, 0.2, 0.2, 1),
                       (0.5, 0.3, 0.0, 1)]

        self.startNew()
        # self.addBlock((0, 10, 0))

    def startNew(self):
        self.land = render.attachNewNode('Land')

    def getColor(self, z):
        if z < len(self.colors):
            return self.colors[z]
        else:
            return self.colors[0]

    def clear(self):
        self.land.removeNode()
        self.startNew()

    def addBlock(self, position):
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))
        self.block.setPos(position)
        color = self.getColor(int(position[2]))
        self.block.setColor(color)
        self.block.setTag('at', str(position))
        self.block.reparentTo(self.land)

    def findBlocks(self, pos):
        return self.land.findAllMatches('=at=' + str(pos))

    def isEmpty(self, pos):
        blocks = self.findBlocks(pos)
        if blocks:
            return False
        else:
            return True 

    def findHighestEmpty(self, pos):
        x, y, z = pos # (1, 6, 9)
        z = 1
        while not self.isEmpty((x, y, z)):
            z += 1
        return (x, y, z)

    def buildBlock(self, pos):
        x, y, z = pos
        new = self.findHighestEmpty(pos)
        if new[2] <= z + 1:
            self.addBlock(new)

    def delBlock(self, pos):
        blocks = self.findBlocks(pos)
        for block in blocks:
            block.removeNode()
    
    def delBlockFrom(self, pos):
        x, y, z = self.findHighestEmpty(pos)
        pos = x, y, z - 1
        for block in self.findBlocks(pos):
            block.removeNode()


    def loadLand(self, filename):
        self.clear()
        with open(filename) as file:
            y = 0
            for line in file:
                x = 0
                line = line.split(' ')
                for z in line:
                    for z0 in range(int(z) + 1):
                        block = self.addBlock((x, y, z0))
                    x += 1
                y += 1