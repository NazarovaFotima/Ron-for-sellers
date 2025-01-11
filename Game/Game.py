from Game_functions import Xazina
from Game_functions import hudud
from Game_functions import print_hudud
from Game_functions import oyin_tasnifi
from Game_functions import Player
from Game_functions import Dushman
from Game_functions import Qilich
from Game_functions import Kuch


# O'yinga kirish
oyin_tasnifi()
Player1 = Player(0, 0)
Player1.print_zaxira()
print("O'yindan chiqish uchun X bosing")
hudud[Player1.y][Player1.x] = "P"
Dushman1 = Dushman(4, 2)
hudud[Dushman1.y][Dushman1.x] = "D"
Dushman2 = Dushman(6, 4)
hudud[Dushman2.y][Dushman2.x] = "D"
Dushman3 = Dushman(3, 6)
hudud[Dushman3.y][Dushman3.x] = "D"
Dushman4 = Dushman(7, 8)
hudud[Dushman4.y][Dushman4.x] = "D"
Qilich1 = Qilich(5, 0, 20)
hudud[Qilich1.y][Qilich1.x] = "Q"
Kuch1 = Kuch(2, 5,20)
hudud[Kuch1.y][Kuch1.x] = "K"
Xazinacha=Xazina(3,2)
hudud[Xazinacha.y][Xazinacha.x]= "kx"
Sup_xazina=Xazina(9,9)
hudud[Sup_xazina.y][Sup_xazina.x]="SX"

print_hudud(hudud)

while True:
    dx=input("O'nga(1) yoki chapga(-1), joyida turish(0): ")
    dy=input("Pastga(1) yoki yuqoriga(-1), joyida turish(0):  ")
    if dx=="X".swapcase() or dy=="X".swapcase() :
        break

    Dushman1.xarakatlanish()
    Dushman2.xarakatlanish()
    Dushman3.xarakatlanish()
    Player1.go(dx, dy)
    if (Player1.y== Dushman1.y and Player1.x== Dushman1.x) or (Player1.y== Dushman2.y and Player1.x== Dushman2.x) or (Player1.y== Dushman3.y and Player1.x== Dushman3.x) or (Player1.y== Dushman4.y and Player1.x== Dushman4.x):
        print("Dushmanga duch keldingiz")
        if Player1.zaxira_sumkasi[1]["kuch"]==0:
            print("O'yinchining joni", Player1.zaxira_sumkasi[1]["kuch"], "ga teng\nO'yin tugadi. Siz yutqazdingiz." )
            break
        Dushman1.hujum(Player1)
        Player1.jang_qil(Dushman1)
    if (Qilich1.y==Dushman1.y and Qilich1.x==Dushman1.x) or (Qilich1.y==Dushman2.y and Qilich1.x==Dushman2.x) or (Qilich1.y==Dushman3.y and Qilich1.x==Dushman3.x) or (Qilich1.y==Dushman4.y and Qilich1.x==Dushman4.x):
        Dushman1.xarakatlanish()
    if (Kuch1.y==Dushman1.y and Kuch1.x==Dushman1.x) or (Kuch1.y==Dushman2.y and Kuch1.x==Dushman2.x) or (Kuch1.y==Dushman3.y and Kuch1.x==Dushman3.x) or (Kuch1.y==Dushman4.y and Kuch1.x==Dushman4.x):
        Dushman1.xarakatlanish()
    if (Xazinacha.y==Dushman1.y and Xazinacha.x==Dushman1.x) or (Xazinacha.y==Dushman2.y and Xazinacha.x==Dushman2.x) or (Xazinacha.y==Dushman3.y and Xazinacha.x==Dushman3.x) or (Xazinacha.y==Dushman4.y and Xazinacha.x==Dushman4.x):
        Dushman1.xarakatlanish()
    if (Sup_xazina.y==Dushman1.y and Sup_xazina.x==Dushman1.x) or (Sup_xazina.y==Dushman2.y and Sup_xazina.x==Dushman2.x) or(Sup_xazina.y==Dushman3.y and Sup_xazina.x==Dushman3.x) or(Sup_xazina.y==Dushman4.y and Sup_xazina.x==Dushman4.x):
        Dushman1.xarakatlanish()
    if Player1.y== Qilich1.y and Player1.x== Qilich1.x:
        Qilich1.ozlashtirilish(Player1)
    if Player1.y== Kuch1.y and Player1.x== Kuch1.x:
        Kuch1.ozlashtirilish(Player1)
    if Player1.y==Xazinacha.y and Player1.x==Xazinacha.x:
        Xazinacha.ozlashtirilish(Player1)
    if Player1.y==Sup_xazina.y and Player1.x==Sup_xazina.x:
        Sup_xazina.s_xazina(Player1)
        print("O'yin tugadi\nG'OLIBSIZ!!!")
        break

    print_hudud(hudud)