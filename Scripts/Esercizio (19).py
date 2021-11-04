CostoTotale = float(input())
Sconto = int(input())

if Sconto == 0:
    CostoScontato = CostoTotale
elif Sconto == 1:
    CostoScontato = CostoTotale-(CostoTotale*10/100)
elif Sconto == 2:
    CostoScontato = CostoTotale-(CostoTotale*15/100)
elif Sconto == 3:
    CostoScontato = CostoTotale-(CostoTotale*25/100)

print(round(CostoScontato, 3), end='')
