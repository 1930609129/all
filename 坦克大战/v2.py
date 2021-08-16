import pygame

class MainGame:
    window=None
    height=700
    width=400
    color=pygame.Color(22,33,44)
    def __init__(self):
        pass

    def startgame(self):
        pygame.display.init()
        self.window=pygame.display.set_mode([self.width,self.height])
        pygame.display.set_caption('坦克大战')
        while True:
            self.window.fill(self.color)
            pygame.display.update()
    def endgame(self):
        print("谢谢使用")
        exit()
class Tank:
    def __init__(self):
        pass

    def move(self):
        pass

    def shot(self):
        pass

    def displaytank(self):
        pass
class MyTank(Tank):
    def __init__(self):
        pass
class YourTank(Tank):
    def __init__(self):
        pass
class Bullet:
    def __init__(self):
        pass

    def bulletmove(self):
        pass

    def displaybullet(self):
        pass
class Wall:
    def __init__(self):
        pass

    def displaywall(self):
        pass
class Explode:
    def __init__(self):
        pass

    def displayexplode(self):
        pass
class Music:
    def __init__(self):
        pass

    def playmusic(self):
        pass
MainGame().startgame()