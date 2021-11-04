Lista = []
Divisibile = False
for k in range (0,10):
    Lista.append(int(input()))
X = int(input())

for Elemento in Lista:
    if Elemento % X == 0:
        Divisibile = True

if not Divisibile:
    print('OK', end='')
else:
    print('NO', end='')
