import pygame

class MainGame:
    window=None
    height=800
    width=500
    version='1.1'
    color=pygame.Color(22,33,44)
    textcolor=pygame.Color(255,0,0)
    Tank_P1=None
    def __init__(self):
        pass

    def startgame(self):
        pygame.display.init()
        MainGame.window=pygame.display.set_mode([self.width,self.height])
        self.Tank_P1=Tank(400,300)
        pygame.display.set_caption('坦克大战'+self.version)
        while True:
            self.window.fill(self.color)
            self.window.blit(self.getText('剩余坦克%d'%5),(5,5))
            self.getEvent()
            self.Tank_P1.displaytank()
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
class Tank():
    def __init__(self,left,top):
        self.images={
            'U':pygame.image.load('./U.png'),
            'D':pygame.image.load('./D.png'),
            'L':pygame.image.load('./L.png'),
            'R':pygame.image.load('./R.png')
        }
        self.direction='U'
        self.image=self.images[self.direction]
        self.rect=self.image.get_rect()
        self.rect.left=left
        self.rect.top=top

    def move(self):
        pass

    def shot(self):
        pass

    def displaytank(self):
        self.image=self.images[self.direction]
        MainGame.window.blit(self.image,self.rect)
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