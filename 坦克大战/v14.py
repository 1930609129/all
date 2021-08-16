import pygame,time,random

class MainGame:
    window=None
    HETGHT=500
    WIDTH=800
    version='1.1'
    color=pygame.Color(22,33,44)
    textcolor=pygame.Color(255,0,0)
    Tank_P1=None
    YourTank_list=[]
    YourTank_count=5
    Bullet_list=[]
    def __init__(self):
        pass

    def startgame(self):
        pygame.display.init()
        MainGame.window=pygame.display.set_mode([MainGame.WIDTH,MainGame.HETGHT])
        MainGame.Tank_P1=Tank(300,400)
        self.creatYourtank()
        pygame.display.set_caption('坦克大战'+MainGame.version)
        while True:
            MainGame.window.fill(MainGame.color)
            self.getEvent()
            MainGame.window.blit(self.getText('剩余坦克%d' % len(MainGame.YourTank_list)), (5, 5))
            MainGame.Tank_P1.displaytank()
            self.blitYourtank()
            if MainGame.Tank_P1 and not MainGame.Tank_P1.stop:
                MainGame.Tank_P1.move()
            self.blitBullet()
            time.sleep(0.02)

            pygame.display.update()
    def creatYourtank(self):
        top=100
        for i in range(MainGame.YourTank_count):
            left = random.randint(1, 7)
            speed = random.randint(3, 6)
            eTank=YourTank(left*100,top,speed)
            MainGame.YourTank_list.append(eTank)
    def blitYourtank(self):
        for eTank in MainGame.YourTank_list:
            eTank.displaytank()
            eTank.randmove()
        # for etank in MainGame.YourTank_list:
        #     etank.displaytank()
        #     etank.randmove()
    def blitBullet(self):
        for bullet in MainGame.Bullet_list:
            if bullet.live:
                bullet.displaybullet()
                bullet.bulletmove()
            else:
                MainGame.Bullet_list.remove(bullet)
    def getEvent(self):

        Eventlist=pygame.event.get()
        for event in Eventlist:
            if event.type==pygame.QUIT:
                self.endgame()

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    MainGame.Tank_P1.direction='L'
                    MainGame.Tank_P1.stop=False
                    print("左")
                elif event.key==pygame.K_RIGHT:
                    MainGame.Tank_P1.direction = 'R'
                    MainGame.Tank_P1.stop = False
                    print("右")
                elif event.key==pygame.K_UP:
                    MainGame.Tank_P1.direction = 'U'
                    MainGame.Tank_P1.stop = False
                    print("上")
                elif event.key==pygame.K_DOWN:
                    MainGame.Tank_P1.direction = 'D'
                    MainGame.Tank_P1.stop = False
                    print("下")
                elif event.key==pygame.K_SPACE:
                    if len(MainGame.Bullet_list)<3:
                        m=Bullet(MainGame.Tank_P1)
                        MainGame.Bullet_list.append(m)
                    print("发射")
                    print('%s'%len(MainGame.Bullet_list))
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_UP or event.key==pygame.K_DOWN or event.key==pygame.K_RIGHT:
                    MainGame.Tank_P1.stop=True

    def getText(self,text):
        pygame.font.init()
        font=pygame.font.SysFont('kaiti',18)
        textsurface=font.render(text,True,MainGame.textcolor)
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
        self.speed=5
        self.stop=True

    def move(self):
        if self.direction=='U':
            if self.rect.top>0:
                self.rect.top-=self.speed
        elif self.direction=='D':
            if self.rect.top+self.rect.height<MainGame.HETGHT:
                self.rect.top+=self.speed
        elif self.direction=='L':
            if self.rect.left>0:
                self.rect.left-=self.speed
        elif self.direction=='R':
            if self.rect.left+self.rect.height<MainGame.WIDTH:
                self.rect.left+=self.speed

    def shot(self):
        pass

    def displaytank(self):
        self.image=self.images[self.direction]
        MainGame.window.blit(self.image,self.rect)
class MyTank(Tank):
    def __init__(self):
        pass
class YourTank(Tank):

    def __init__(self,left,top,speed):
        self.images = {
            'U': pygame.image.load('./1U.png'),
            'D': pygame.image.load('./2D.png'),
            'L': pygame.image.load('./3L.png'),
            'R': pygame.image.load('./1R.png')
        }
        self.direction = self.randdirection()
        self.image = self.images[self.direction]
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top
        self.speed = speed
        self.stop = True
        self.step=50
    def randdirection(self):
        mun=random.randint(1,4)
        if mun==1:
            return 'U'
        elif mun==2:
            return 'D'
        elif mun==3:
            return 'L'
        elif mun==4:
            return 'R'
    def randmove(self):
        if self.step<=0:
            self.direction = self.randdirection()
            self.step=50
        else:
            self.move()
            self.step-=1

class Bullet:
    def __init__(self,tank):
        self.image=pygame.image.load('./1.png')
        self.direction=tank.direction
        self.rect=self.image.get_rect()
        self.speed=8
        self.live=True
        if self.direction=='U':
            self.rect.left=tank.rect.left+tank.rect.width/2 -self.rect.width/2
            self.rect.top=tank.rect.top-self.rect.height
        elif self.direction=='D':
            self.rect.top=tank.rect.top+tank.rect.height
            self.rect.left=tank.rect.left+tank.rect.width/2-self.rect.width/2
        elif self.direction=='L':
            self.rect.left = tank.rect.left - self.rect.width/2-self.rect.width/2
            self.rect.top = tank.rect.top + tank.rect.height/2 -self.rect.width/2
        elif self.direction=='R':
            self.rect.left = tank.rect.left + tank.rect.width
            self.rect.top = tank.rect.top + tank.rect.height/2 -self.rect.width/2
    def bulletmove(self):
        if self.direction=='U':
            if self.rect.top>0:
                self.rect.top-=self.speed
            else:
                self.live=False
        elif self.direction=='D':
            if self.rect.top<MainGame.HETGHT-self.rect.height:
                self.rect.top+=self.speed
            else:
                self.live=False
        elif self.direction=='L':
            if self.rect.left>0:
                self.rect.left-=self.speed
            else:
                self.live=False
        elif self.direction=='R':
            if self.rect.left<MainGame.WIDTH-self.rect.width:
                self.rect.left+=self.speed
            else:
                self.live=False

    def displaybullet(self):
        MainGame.window.blit(self.image,self.rect)
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