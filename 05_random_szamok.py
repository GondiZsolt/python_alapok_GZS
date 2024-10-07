"""
1. Feladat
Készíts egy rövid programot, amely 1 és 3 között generál véletlenszámot, majd összehasonlítja ezt a felhasználó által megadott, szintén ebbe a tartományba eső számmal! Az összehasonlítás eredményéről tájékoztassa a felhasználót!
"""

import random
random_szam = random.randint(1, 3)

szam = int(input("Adj meg egy egész számot 1 és 3 között!"))
if szam == random_szam:
    print("Ugyan arra gondoltunk :)")
else:
    print("Nem ugyan arra gondoltunk :(")
print(random_szam)