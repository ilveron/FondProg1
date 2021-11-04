Tappo = -50
N = int(input())
Numeri = []
MaggioriMedia = []

while N != Tappo:
    Numeri.append(N)
    N = int(input())

if len(Numeri) > 0:
    MediaNumeri = sum(Numeri)//len(Numeri) 

    for Elemento in Numeri:
        if Elemento >= MediaNumeri:
            MaggioriMedia.append(Elemento)

    print(min(MaggioriMedia), end='')
else:
    print('VUOTA', end='')
    
