# sor = 1
# while sor <= 5:
#      oszlop = 1
#      while oszlop <= 7:
#          print('O ', end='')
#          oszlop = oszlop + 1
#      print('')
#      sor = sor + 1

# darab_karakter = 1
# sor = 1
# while sor <= 7:
#     oszlop = 1
#     while oszlop <= darab_karakter:
#         print('O ', end='')
#         oszlop = oszlop + 1
#     print('')
#     darab_karakter = darab_karakter + 1
#     sor = sor + 1

"""1. Feladat - Pocak
Készíts egy programot, amely a felhasználótól bekér egy páros számot, majd ennek megfelelően rajzol ki a képernyőre egy pocak szerű alakzatot az alábbiak szerint!
"""

felh_inp = int(input("Adj meg egy páros számot!"))

darab_karakter = 1
sor = 1
while sor <= felh_inp:
    oszlop = 1
    while oszlop <= darab_karakter:
        print('O ', end='')
        oszlop = oszlop + 1
    print('')
    darab_karakter = darab_karakter + 1
    sor = sor + 1
if sor == felh_inp:
    while oszlop <= darab_karakter:
        print('O ', end='')
        oszlop = oszlop - 1
    print('')
    darab_karakter = darab_karakter - 1
    sor = sor - 1