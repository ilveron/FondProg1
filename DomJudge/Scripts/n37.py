Caratteri = []
NumVocaliMin = 0
Vocali = ['a','e','i','o','u']
for k in range (0,100):
    Caratteri.append(input())

for Elemento in Caratteri:
    if Elemento in Vocali:
        NumVocaliMin += 1
        Vocali.remove(Elemento)
        

if NumVocaliMin <= 1:
    print('OK', end='')
else:
    print('ERRORE', end='')
