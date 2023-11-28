import random
import math
print ("Arvaus peli!")
kone_numero = random.randint(0,20)
rundi_maara = 3
print("\n\tSinulla on ",rundi_maara," mahdollisuutta arvata oikea luku!\n")
for i in range(3):
    arvaus = int(input("Arvaa oikea numero (0-20)?: "))
    if arvaus < kone_numero:
            print("\n\tArvaa suurempi luku.\n")
    elif (arvaus < 0) or (arvaus > 20):
            print("\n\tVirhe\n")
    elif arvaus > kone_numero:
            print("\n\tArvaa pienempi luku.\n")
    elif arvaus == kone_numero:
            print("\n\tOikea luku! Voitit\n")
            break
    else:
        print("Hävisit!")


