import pygame

class MainGame:
    window=None
    height=700
    width=400
    version='1.1'
    color=pygame.Color(22,33,44)
    def __init__(self):
        pass

    def startgame(self):
        pygame.display.init()
        self.window=pygame.display.set_mode([self.width,self.height])
        pygame.display.set_caption('坦克大战'+self.version)
        while True:
            self.window.fill(self.color)
            self.getEvent()
            pygame.display.update()

    def getEvent(self):
        Eventlist=pygame.event.get()
        for event in Eventlist:
            if event.type==pygame.QUIT:
                self.endgame()

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    print("左")
                elif event.key==pygame.K_RIGHT:
                    print("右")
                elif event.key==pygame.K_UP:
                    print("上")
                elif event.key==pygame.K_DOWN:
                    print("下")
                elif event.key==pygame.K_SPACE:
                    print("发射")

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