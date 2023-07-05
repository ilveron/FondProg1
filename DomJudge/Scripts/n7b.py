X = int(input())
N = int(input())
cont = 0
Minoripari = ''
while cont < N:
    Elemento = int(input())
    if Elemento % 2 == 0 and Elemento < X:
        Minoripari += str(Elemento)
    cont+=1

print(Minoripari, end='')
