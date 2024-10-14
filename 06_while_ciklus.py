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

# szam = 1
# while szam <= 10:
#     if szam % 2 == 0:
#         print(szam)
#     szam += 1

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

"""5. Feladat
Írj egy programot, amely a felhasználótól páros számot kér be. Amennyiben a megadott szám páratlan,
újra és újra megtörténik az adatbekérés mindaddig, amíg végül páros számot nem ad meg a felhasználó.
"""

paros_szam = False

while paros_szam == False:
    felhasznaloi_input = int(input("Adj meg egy páros számot!"))
    if felhasznaloi_input % 2 == 0:
        paros_szam = True
    if paros_szam == True:
        print("kösz mán")