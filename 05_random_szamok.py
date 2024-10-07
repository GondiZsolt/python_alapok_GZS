"""
1. Feladat
Készíts egy rövid programot, amely 1 és 3 között generál véletlenszámot, majd összehasonlítja ezt a felhasználó által megadott, szintén ebbe a tartományba eső számmal! Az összehasonlítás eredményéről tájékoztassa a felhasználót!
"""

# import random
# random_szam = random.randint(1, 3)
#
# szam = int(input("Adj meg egy egész számot 1 és 3 között!"))
# if szam == random_szam:
#     print("Ugyan arra gondoltunk :)")
# else:
#     print("Nem ugyan arra gondoltunk :(")
# print(random_szam)

"""2. Feladat
A program a pénzfeldobást modellezi. Kérdezze meg a felhasználótól a választását (fej vagy írás), majd adjon tájékoztatást, hogy eltalálta-e!
"""

import random
coin = ["Fej", "Írás"]
flip = random.choice(coin)

kerdes = ("Fej", "Írás")

kerdes == str(input("Fej vagy Írás?"))

if kerdes == flip:
    print("Eltaláltad!")

print(flip)