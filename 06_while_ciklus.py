# szam = 1
# while szam <= 10:
#     print(szam)
#     szam = szam + 1

# folytatja = True
# while folytatja:
#     print('Vidd ki a szemetet!')
#     valasz = input('Mondjam még egyszer? (i/n)')
#     if valasz == 'n':
#         folytatja = False
# print('>> Program vége! <<')

szam = 1
while szam <= 10:
    if szam % 2 == 0:
        print(szam)
    szam += 1

"""2. Feladat
Írj egy programot, amely csökkenő sorrendben írja ki a számokat 1 és 10 között!
"""

# szam = 10
# while szam >=1:
#     print(szam)
#     szam -= 1

"""3. Feladat
Írj egy programot, amely kiírja a páratlan számokat csökkenő sorrendben 1 és 10 között!
"""

# szam = 10
# while szam >=1:
#     if szam % 2 == 1:
#         print(szam)
#     szam -= 1