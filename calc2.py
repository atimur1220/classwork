# program
import math

nr1 = float(input("alegeti un numar: "))
nr2 = float(input("alegeti un alt numar: "))
alegere = int(input("Alegeti una dintre operatiuni (1 - ad, 2 - sc, 3 - inm, 4 - impartire, 5 - ridicare la putere, 6 - logaritm, 7 - radical): "))
if alegere == 1:
    print(nr1 + nr2)
elif alegere == 2:
    print(nr1 - nr2)
elif alegere == 3:
    print(nr1 * nr2)
elif alegere == 4:
    print(nr1 / nr2)
elif alegere == 5:
    print(nr1 ** nr2)
elif alegere == 6:
    print(math.log(nr1, nr2))
elif alegere == 7:
    print(math.sqrt(nr1))
else:
    print("nu ati ales o operatiune")
