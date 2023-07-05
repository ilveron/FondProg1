A = []
B = []
NumLettereAlfabeto = 26
Risultato = ''

for k in range (26):
    A.append(input())

N = int(input())

for k in range(N):
    B.append(int(input()))

for Elemento in B:
    if Elemento < NumLettereAlfabeto:
        Risultato+=A[Elemento]

print(Risultato, end='')
        
        
