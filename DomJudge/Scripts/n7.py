N = int(input())
Multipli = 0

while N != 5:
    if N % 5 == 0:
        Multipli+=1
    N = int(input())

if Multipli==0:
    print('NESSUNO', end='')
else:
    print('ALMENO 1', end='')

    
