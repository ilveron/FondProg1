Lista = []
N = int(input())
Tappo = 0

while N != Tappo:
    Lista.append(N)
    N = int(input())

LunghezzaLista = len(Lista)
ElementiUguali = False

for i in range (LunghezzaLista-1):
    if ElementiUguali:
        break
    
    Elemento1 = Lista[i]
    for j in range (i+1, LunghezzaLista):
        Elemento2 = Lista[j]
        if Elemento1 == Elemento2:
            ElementiUguali = True
            break

if ElementiUguali:
    print('Ci sono due elementi uguali')
else:
    print('NON ci sono due elementi uguali')
            
