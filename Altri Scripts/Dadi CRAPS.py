from random import randint

Dado1 = randint(1,6)
Dado2 = randint(1,6)
Lancio = Dado1+Dado2
NumLanci = 1
if Lancio == 7 or Lancio == 11:
    print('COMPLIMENTI, HAI VINTO!!!')
elif Lancio == 2 or Lancio == 3 or Lancio == 12:
    print('PECCATO, HAI PERSO...')
else:
    P = Lancio
    Lancio = 0
    while Lancio != P and Lancio != 7:
        Dado1 = randint(1,6)
        Dado2 = randint(1,6)
        Lancio = Dado1+Dado2
        NumLanci+=1
    if Lancio == P:
        print('COMPLIMENTI, HAI VINTO!!!')
    else:
        print('PECCATO, HAI PERSO...')

print('Hai tirato', Lancio, 'dopo', NumLanci, 'lanci')
