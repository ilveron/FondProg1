def StampaSequenzaMaggiore(S):
    InStringa = ''
    for Elemento in S:
        InStringa+=str(Elemento)
    
    print(InStringa)
    print(len(S), end='')

N = int(input())
Elementi = []
while N >= 0:
    Elementi.append(N)
    N = int(input())

SequenzaMaggiore = []

PosIniziale = 0
NumElementi = len(Elementi)
if NumElementi >= 2:
    Sequenza = [Elementi[0]]
    k = 0
    while k < NumElementi-1:
        if Elementi[k+1] >= Elementi[k]:
            Sequenza.append(Elementi[k+1])
        else:
            if k+1 != NumElementi-1:
                Sequenza = [Elementi[k+1]]

        if len(Sequenza) > len(SequenzaMaggiore):
                SequenzaMaggiore = Sequenza.copy()
        k+=1
    if len(SequenzaMaggiore) == 1:
        SequenzaMaggiore = [Elementi[0]]
        
    StampaSequenzaMaggiore(SequenzaMaggiore)
elif NumElementi == 1:
    SequenzaMaggiore = [Elementi[0]]
    StampaSequenzaMaggiore(SequenzaMaggiore)
else:
    print('Empty', end='')


