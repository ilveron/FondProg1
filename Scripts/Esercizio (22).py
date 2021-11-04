Briscola = int(input())

Seme1 = int(input())
Carta1 = int(input())
if Carta1 == 1:
    Carta1 = 11
elif Carta1 == 3:
    Carta1 = float(10.5)

Seme2 = int(input())
Carta2 = int(input())
if Carta2 == 1:
    Carta2 = 11
elif Carta2 == 3:
    Carta2 = float(10.5)

if Seme1 == Seme2:
    if Carta1 > Carta2:
        print('VINCE GIOCATORE 1', end='')
    else:
        print('VINCE GIOCATORE 2', end='')
elif Seme2 != Briscola:
    print('VINCE GIOCATORE 1', end='')
else:
    print('VINCE GIOCATORE 2', end='')
    
    



