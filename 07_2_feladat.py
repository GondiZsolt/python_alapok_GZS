"""2. Feladat - \
Készíts egy programot, amely egymásba ágyazott ciklusok segítségével rajzolja ki egy 5 x 5-ös mezőben az alábbi alakzatot!
"""

# for i in range(5):
#     for j in range(5):
#         if i == j:
#             print("O", end=" ")
#         else:
#             print(".", end=" ")
#     print()

"""3. Feladat - X
Készíts egy programot, amely egymásba ágyazott ciklusok segítségével rajzolja ki egy 7 x 7-es mezőben az alábbi alakzatot!
"""

# for i in range(7):
#     for j in range(7):
#         if i == j:
#             print("O", end=" ")
#         elif i + j == 6:
#             print("O", end=" ")
#         else:
#             print(".", end=" ")
#     print()

szam = int(input("Adjál megfele egy páratlan számot!"))

for i in range(szam):
    for j in range(szam):
        if i == j:
            print("O", end=" ")
        elif i + j == szam - 1:
            print("O", end=" ")
        else:
            print(".", end=" ")
    print()
print("Tessék!")