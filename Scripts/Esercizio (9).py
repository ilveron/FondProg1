#Conto appena creato (1° mese)
Conto = int(input())
Canone = int(input())
Interesse = int(input())
print('PRIMO MESE:', Conto)

#Secondo mese
Conto -= Canone
Conto += (Conto/100)*Interesse
print('SECONDO MESE:', round(Conto))

#Terzo Mese
Conto -= Canone
Conto += (Conto/100)*Interesse
print('TERZO MESE:', round(Conto), end='')

