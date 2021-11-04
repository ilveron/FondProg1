N = input()
Numero = []
LunghezzaNumero = len(N)
for k in range (0, LunghezzaNumero):
    Numero.append(int(N[k]))

MezzoNumero = LunghezzaNumero//2

Somma1 = sum(Numero[0:MezzoNumero])
Somma2 = sum(Numero[MezzoNumero:])

if Somma1 == Somma2:
    print('FORTUNATO', end='')
else:
    print('SFORTUNATO', end='')
