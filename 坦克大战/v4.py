import pygame

class MainGame:
    window=None
    height=800
    width=500
    version='1.1'
    color=pygame.Color(22,33,44)
    textcolor=pygame.Color(255,0,0)
    def __init__(self):
        pass

    def startgame(self):
        pygame.display.init()
        self.window=pygame.display.set_mode([self.width,self.height])
        pygame.display.set_caption('坦克大战'+self.version)
        while True:
            self.window.fill(self.color)
            self.window.blit(self.getText('剩余坦克%d'%5),(5,5))
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

    def getText(self,text):
        pygame.font.init()
        font=pygame.font.SysFont('kaiti',18)
        textsurface=font.render(text,True,self.textcolor)
        return textsurface

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