from random import randint
Base = randint(-9999, 9999)
Basi = []
Basi.append(Base)
Esponenti = []
Divisori = []
Risultati = []

while Base != 0:
    Esponente = randint(-9999, 9999)
    Esponenti.append(Esponente)
    for Elemento in Esponenti:
        print(Elemento, end = ' ')
    print()
    Divisore = randint(-9999, 9999)
    Divisori.append(Divisore)
    for Elemento in Esponenti:
        print(Elemento, end = ' ')
    print()
    Risultato = (Base^Esponente)/Divisore
    Risultati.append(Risultato)
    for Elemento in Risultati:
        print(Elemento, end = ' ')
    print()
    print('Base:', Base)
    print('Esponente:', Esponente)
    print('Risultato:', Risultato)
    Base = randint(-9999, 9999)
    Basi.append(Base)
    for Elemento in Basi:
        print(Elemento, end = ' ')
    print()
