X = int(input())
while X < 0:
    X = int(input())
    
SottosequenzaPari = []
SottosequenzaDispari = []
Crescenti = True
Dispari = True

for k in range (0,X):
    N = int(input())
    if k%2 == 0:
        SottosequenzaPari.append(N)
    else:
        SottosequenzaDispari.append(N)


for k in range(0, len(SottosequenzaPari)):
    if k != 0:
        if SottosequenzaPari[k] <= SottosequenzaPari[k-1]:
            Crescenti = False
            break

for Elemento in SottosequenzaDispari:
    if Elemento%2 != 1:
        Dispari = False

if Crescenti and Dispari:
    print('SI',end='')
else:
    print('NO',end='')
        
            
    
        
    
