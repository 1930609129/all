import pygame,time,random
version='v1.1'
class MainGame():
    window=None
    WIDTH=800
    HETGHT=500
    Color=pygame.Color(11,22,33)
    Colorred=pygame.Color(255,0,0)
    Tank_P1 = None
    YourTanK_list=[]
    YourTanK_mun=5
    Bullet_list=[]
    Your_Bullet_list=[]
    Explode_list=[]
    Wall_list=[]
    def __init__(self):
        pass

    def startgame(self):
        pygame.display.init()
        MainGame.window=pygame.display.set_mode([MainGame.WIDTH,MainGame.HETGHT])
        self.creatMytank()
        self.creatYourtank()
        self.creatWall()
        pygame.display.set_caption('坦克大战'+version)
        while True:
            MainGame.window.fill(MainGame.Color)
            self.getEvent()
            self.blitWall()
            MainGame.window.blit(self.getText('剩余敌方坦克%d辆'%len(MainGame.YourTanK_list)),(5,5))
            if MainGame.Tank_P1 and MainGame.Tank_P1.live:
                MainGame.Tank_P1.displayTank()

            else:
                del MainGame.Tank_P1
                MainGame.Tank_P1=None
            self.biltYourtank()
            self.blitBullet()
            if MainGame.Tank_P1 and not MainGame.Tank_P1.stop:
                MainGame.Tank_P1.move()
                MainGame.Tank_P1.hitwalls()
                MainGame.Tank_P1.hitYourTank()
            time.sleep(0.02)
            self.YourblitBullet()
            self.dispExplodes()
            pygame.display.update()
    def creatYourtank(self):
        top=100
        for i in range(MainGame.YourTanK_mun):
            speed = random.randint(3, 6)
            left = random.randint(1, 7)
            eTank=YourTanK(left*100,top,speed)
            MainGame.YourTanK_list.append(eTank)
    def biltYourtank(self):
        for eTank in MainGame.YourTanK_list:
            if eTank.live:
                eTank.hitMyTanK1()
                eTank.displayTank()
                eTank.randmove()
                eTank.hitwalls()
                eBullet=eTank.shot()
                if eBullet:
                    MainGame.Your_Bullet_list.append(eBullet)
            else:
                MainGame.YourTanK_list.remove(eTank)
    def creatMytank(self):
        MainGame.Tank_P1 = MyTank(300, 400)
        music=Music('./1/宗次郎 - 故郷の原風景 (故乡的原风景).mp3')
        music.play()
    def creatWall(self):
        for i in range(5):
            wall=Wall(170*i,240)
            MainGame.Wall_list.append(wall)
    def blitWall(self):
        for wall in MainGame.Wall_list:
            if wall.live:
                wall.dispWall()
            else:
                MainGame.Wall_list.remove(wall)
    def blitBullet(self):
        for bullet in MainGame.Bullet_list:
            if bullet.live:
                bullet.dispBullet()
                bullet.move()
                bullet.hitYourTank()
                bullet.hitwall()
            else:
                MainGame.Bullet_list.remove(bullet)
    def YourblitBullet(self):
        for ebullet in MainGame.Your_Bullet_list:
            if ebullet.live:
                ebullet.dispBullet()
                ebullet.move()
                ebullet.hitwall()
                if MainGame.Tank_P1 and MainGame.Tank_P1.live:
                    ebullet.hitMyTank()
            else:
                MainGame.Your_Bullet_list.remove(ebullet)
    def dispExplodes(self):
        for explode in MainGame.Explode_list:
            if explode.live:
                explode.dispExplode()
            else:
                MainGame.Explode_list.remove(explode)
    def getText(self,text):
        pygame.font.init()
        font=pygame.font.SysFont('kaiti',18)
        textnew=font.render(text,True,MainGame.Colorred)
        return textnew
    def getEvent(self):
        eventlist=pygame.event.get()
        for event in eventlist:
            if event.type==pygame.QUIT:
                self.endgame()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE and not MainGame.Tank_P1:
                    self.creatMytank()
                if MainGame.Tank_P1 and MainGame.Tank_P1.live:
                    if event.key==pygame.K_LEFT:
                        MainGame.Tank_P1.direction='L'
                        # MainGame.Tank_P1.move()
                        MainGame.Tank_P1.stop=False
                        print("向左移动")
                    elif event.key==pygame.K_RIGHT:
                        MainGame.Tank_P1.direction = 'R'
                        # MainGame.Tank_P1.move()
                        MainGame.Tank_P1.stop = False
                        print("向右移动")
                    elif event.key==pygame.K_UP:
                        MainGame.Tank_P1.direction = 'U'
                        # MainGame.Tank_P1.move()
                        MainGame.Tank_P1.stop = False
                        print("向上移动")
                    elif event.key==pygame.K_DOWN:
                        MainGame.Tank_P1.direction = 'D'
                        # MainGame.Tank_P1.move()
                        MainGame.Tank_P1.stop = False
                        print("向下移动")
                    elif event.key==pygame.K_SPACE:
                        print("发射子弹")
                        if len(MainGame.Bullet_list)<3:
                            m=Bullet(MainGame.Tank_P1)
                            MainGame.Bullet_list.append(m)
                            # music = Music('./1/宗次郎 - 故郷の原風景 (故乡的原风景).mp3')
                            # music.play()
                        else:
                            print('子弹不足')
                        print('当前子弹数量%d'%len(MainGame.Bullet_list))
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT or event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                    if MainGame.Tank_P1 and MainGame.Tank_P1.live:
                        MainGame.Tank_P1.stop = True
                # if not event.key==pygame.K_SPACE:
                #     MainGame.Tank_P1.stop=True
    def endgame(self):
        print("谢谢使用")
        exit()
class BaseItem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
class Tank(BaseItem):
    def __init__(self,left,top):

        self.speed=5
        self.live = True
        self.images={
            'U':pygame.image.load('./U.png'),
            'D':pygame.image.load('./D.png'),
            'L':pygame.image.load('./L.png'),
            'R':pygame.image.load('./R.png')
        }
        self.direction='U'
        self.image=self.images[self.direction]
        self.rect=self.image.get_rect()
        self.rect.left = left
        self.rect.top = top
        self.stop=True
        self.oldleft=self.rect.left
        self.oldtop=self.rect.top

    def move(self):
        self.oldleft = self.rect.left
        self.oldtop = self.rect.top
        if self.direction=='L':
            if self.rect.left>0:
                self.rect.left-=self.speed
        elif self.direction=='R':
            if self.rect.left+self.rect.height<MainGame.WIDTH:
                self.rect.left+=self.speed
        elif self.direction=='U':
            if self.rect.top>0:
                self.rect.top-=self.speed
        elif self.direction=='D':
            if self.rect.top+self.rect.height<MainGame.HETGHT:
                self.rect.top+=self.speed
    def stay(self):
        self.rect.left=self.oldleft
        self.rect.top=self.oldtop
    def hitwalls(self):
        for wall in MainGame.Wall_list:
            if pygame.sprite.collide_rect(wall,self):
                self.stay()
    def shot(self):
        return Bullet(self)
    def displayTank(self):
        self.image=self.images[self.direction]
        MainGame.window.blit(self.image,self.rect)
class MyTank(Tank):
    def __init__(self,left,top):
        super(MyTank,self).__init__(left,top)
    def hitYourTank(self):
        for eTank in MainGame.YourTanK_list:
            if pygame.sprite.collide_rect(eTank,self):
                self.stay()
class YourTanK(Tank):
    def __init__(self,left,top,speed):
        super(YourTanK,self).__init__(left,top)
        self.speed = speed
        self.images = {
            'U': pygame.image.load('./1U.png'),
            'D': pygame.image.load('./2D.png'),
            'L': pygame.image.load('./3L.png'),
            'R': pygame.image.load('./1R.png')
        }
        self.direction = self.rand()
        self.image = self.images[self.direction]
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top
        self.stop = True
        self.step=50
    def rand(self):
        mun=random.randint(1,4)
        if mun==1:
            return 'U'
        elif mun==2:
            return 'D'
        elif mun==3:
            return 'L'
        elif mun==4:
            return 'R'
    # def displayYour(self):
    #     super().displayTank()
    def randmove(self):
        if self.step<=0:
            self.direction=self.rand()
            self.step=50
        else:
            self.move()
            self.step-=1
    def shot(self):
        num=random.randint(1,100)
        if num<=3:
            return Bullet(self)
    def hitMyTanK1(self):
        if MainGame.Tank_P1:
            if pygame.sprite.collide_rect(MainGame.Tank_P1,self):
                self.stay()
class Bullet(BaseItem):
    def __init__(self,tank):
        self.image=pygame.image.load('./1.png')
        self.direction=tank.direction
        self.rect=self.image.get_rect()
        self.speed=5
        self.live=True
        if self.direction=='U':
            self.rect.left=tank.rect.left+tank.rect.width/2-self.rect.width/2
            self.rect.top=tank.rect.top-self.rect.height
        elif self.direction=='D':
            self.rect.left = tank.rect.left + tank.rect.width / 2 - self.rect.width / 2
            self.rect.top = tank.rect.top + tank.rect.height
        elif self.direction=='L':
            self.rect.left = tank.rect.left - self.rect.width/2-self.rect.width/2
            self.rect.top = tank.rect.top + tank.rect.width/2 -self.rect.width/2
        elif self.direction=='R':
            self.rect.left = tank.rect.left + tank.rect.width
            self.rect.top = tank.rect.top + tank.rect.width/2 -self.rect.width/2
    def move(self):
        if self.direction == 'U':
            if self.rect.top>0:
                self.rect.top-=self.speed
            else:
                self.live=False
        elif self.direction == 'D':
            if self.rect.top<MainGame.HETGHT-self.rect.height:
                self.rect.top+=self.speed
            else:
                self.live=False
        elif self.direction == 'L':
            if self.rect.left>0:
                self.rect.left-=self.speed
            else:
                self.live = False
        elif self.direction == 'R':
            if self.rect.left<MainGame.WIDTH-self.rect.width:
                self.rect.left+=self.speed
            else:
                self.live=False
    def dispBullet(self):
        MainGame.window.blit(self.image,self.rect)
    def hitYourTank(self):
        for eTank in MainGame.YourTanK_list:
            if pygame.sprite.collide_rect(eTank,self):
                explode=Explode(eTank)
                MainGame.Explode_list.append(explode)
                self.live=False
                eTank.live=False
    def hitMyTank(self):
        if pygame.sprite.collide_rect(self,MainGame.Tank_P1):
            explode=Explode(MainGame.Tank_P1)
            MainGame.Explode_list.append(explode)
            self.live=False
            MainGame.Tank_P1.live=False
    def hitwall(self):
        for wall in MainGame.Wall_list:
            if pygame.sprite.collide_rect(wall,self):
                self.live=False
                wall.hp-=1
                if wall.hp<=0:
                    wall.live=False

class Explode():
    def __init__(self,tank):
        self.rect=tank.rect
        self.step=0
        self.images=[
            pygame.image.load('1/2.png'),
            pygame.image.load('1/1.png'),
            pygame.image.load('1/3.png'),
            pygame.image.load('1/4.png'),
            pygame.image.load('1/5.png')
        ]
        self.image=self.images[self.step]
        self.live = True
    def dispExplode(self):
        if self.step<len(self.images):
            MainGame.window.blit(self.image,self.rect)
            self.image=self.images[self.step]
            self.step+=1
        else:
            self.live=False
            self.step=0
class Wall():
    def __init__(self,left,top):
        self.image=pygame.image.load('1/6.png')
        self.rect=self.image.get_rect()
        self.rect.left=left
        self.rect.top=top
        self.live=True
        self.hp=3
    def dispWall(self):
        MainGame.window.blit(self.image,self.rect)
class Music():
    def __init__(self,filename):
        self.filename=filename
        pygame.mixer.init()
        pygame.mixer.music.load(self.filename)
    def play(self):
        pygame.mixer.music.play()
MainGame().startgame()