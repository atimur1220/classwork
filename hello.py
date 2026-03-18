# program
nr1 = float(input("alegeti un numar: "))
nr2 = float(input("alegeti un alt numar: "))
alegere = int(input("Alegeti una dintre operatiuni (1 - ad, 2 - sc, 3 - inm): "))
if alegere == 1:
    print(nr1 + nr2)
elif alegere == 2:
    print(nr1 - nr2)
elif alegere == 3:
    print(nr1 * nr2)
else:
    print("nu ati ales o operatiune")
