class Camera():
    def __init__(self, x, y, playerdims, windims):
        self.x = x
        self.y = y
        self.playerDims = playerdims
        self.windims = windims

    def update(self, playerX, playerY)  :
        self.x = playerX
        self.y = playerY

    def translate(self, x, y):
        return (x - self.x + self.windims[0] / 2 - self.playerDims[0] / 2,
                y - self.y + self.windims[1] / 2 - self.playerDims[1] / 2)
