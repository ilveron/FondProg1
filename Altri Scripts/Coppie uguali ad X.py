from random import *

X = randint(0, 30)
print('X:', X)
N = int(input())

Conteggio = 0
NumPrecedente = 0
NumCorrente = 0

for NumLetti in range(0, N):
    NumPrecedente = NumCorrente
    NumCorrente = int(input())
    if (NumCorrente + NumPrecedente) == X and NumLetti != 0:
        Conteggio+=1

print('X:', X)
print('Conteggio:', Conteggio)



