
from random import randint, random

hudud=[
    ["*","*","*","*","*","*","*","*","*","*"],
    ["*","*","*","*","*","*","*","*","*","*"],
    ["*","*","*","*","*","*","*","*","*","*"],
    ["*","*","*","*","*","*","*","*","*","*"],
    ["*","*","*","*","*","*","*","*","*","*"],
    ["*","*","*","*","*","*","*","*","*","*"],
    ["*","*","*","*","*","*","*","*","*","*"],
    ["*","*","*","*","*","*","*","*","*","*"],
    ["*","*","*","*","*","*","*","*","*","*"],
    ["*","*","*","*","*","*","*","*","*","*"],

]



def print_hudud(hudud):
    for i in hudud:
        print(" ".join(i))

def oyin_tasnifi():
    print("Alibobo va Qirqqaroqchi o'yini")
    print("P => O'yinchi\nD => Dushman\nQ => Qilich\nK => Kuch\nkx => Kichik xazina\nSX => Marra")

class Player:
    def __init__(self, x, y, zaxira_sumkasi=[]):
        self.zaxira_sumkasi=zaxira_sumkasi
        self.x=x
        self.y=y
        self.zaxira_sumkasi=[{"Qilich_kuchi": 0}, {"kuch": 100}, {"score": 0}, {"xazina": 0}]

    def go(self, dx, dy):
        hudud[self.y][self.x]="*"
        self.y+=int(dy)
        self.x+=int(dx)
        hudud[self.y][self.x] = "P"

    def jang_qil(self, dushman):
        if dushman.ziyon<=self.zaxira_sumkasi[0]["Qilich_kuchi"]:
            self.zaxira_sumkasi[0]["Qilich_kuchi"]-=dushman.ziyon
            self.zaxira_sumkasi[2]["score"]+=1
            self.print_zaxira()

    def print_zaxira(self):
        print("O'yinchining joni: ",self.zaxira_sumkasi[1]["kuch"],"\nQilich kuchi: ", self.zaxira_sumkasi[0]["Qilich_kuchi"],"\nBall: ", self.zaxira_sumkasi[2]["score"], "\nXazina: ", self.zaxira_sumkasi[3]["xazina"])

    def qilich(self, Qilich_kuchi,):
        self.zaxira_sumkasi[0]["Qilich_kuchi"]+=Qilich_kuchi
        self.print_zaxira()

    def kuchi(self, kuch):
        self.zaxira_sumkasi[1]["kuch"] += kuch
        self.print_zaxira()

    def xazina(self, xazina):
        self.zaxira_sumkasi[3]["xazina"] += xazina
        self.print_zaxira()



class Dushman:
    def __init__(self,  x, y, sogliq=100, ziyon=20,):
        self.sogliq=sogliq
        self.ziyon=ziyon
        self.x=x
        self.y=y


    def xarakatlanish(self):
        dx=randint(-1, 1)
        dy=randint(-1, 1)
        hudud[self.y][self.x] = "*"
        try:
            self.y += int(dy)
            self.x += int(dx)
            hudud[self.y][self.x] = "D"
        except IndexError:
            hudud[self.y][self.x] = "D"




    def hujum(self, player):
        if player.zaxira_sumkasi[0]["Qilich_kuchi"]<self.ziyon:
            player.zaxira_sumkasi[1]["kuch"]-=self.ziyon
            player.print_zaxira()


class Anjomlar:
    def __init__(self, x, y):
        self.x=x
        self.y=y

class Qilich(Anjomlar):
    def __init__(self, x,y, kuchi):
        super().__init__(x,y,)
        self.kuchi=kuchi

    def ozlashtirilish(self, player):
        player.qilich(self.kuchi)
        dx = randint(-10, 10)
        dy = randint(-10, 10)
        try:
            self.y += int(dy)
            self.x += int(dx)
            hudud[self.y][self.x] = "Q"
        except IndexError:
            hudud[self.y][self.x] = "Q"

class Kuch(Anjomlar):
    def __init__(self, x, y, kuchi):
        super().__init__(x, y, )
        self.kuchi=kuchi

    def ozlashtirilish(self, player):
        player.kuchi(self.kuchi)
        dx = randint(-10, 10)
        dy = randint(-10, 10)
        try:
            self.y += int(dy)
            self.x += int(dx)
            hudud[self.y][self.x] = "K"
        except IndexError:
            hudud[self.y][self.x] = "K"

class Xazina:
    def __init__(self, x, y, xazinachalar=10, super_xazina=1000):
        self.x=x
        self.y=y
        self.xazinachalar=xazinachalar
        self.super_xazina=super_xazina


    def ozlashtirilish(self, player):
        player.xazina(self.xazinachalar)
        dx = randint(-10, 10)
        dy = randint(-10, 10)
        try:
            self.y += int(dy)
            self.x += int(dx)
            hudud[self.y][self.x] = "kx"
        except IndexError:
            hudud[self.y][self.x] = "kx"

    def s_xazina(self, player):
        player.xazina(self.super_xazina)

