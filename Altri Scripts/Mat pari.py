Mat =[
        [3, 2, 8, 6, 3],
        [2, 4, 4, 5, 9],
        [4, 0, 0, 0, 1],
        [2, 3, 8, 0, 1],
        [5, 1, 4, 7, 0]
     ]

N = len(Mat)
Colonne = N-1

Pari = True

for i in range (0, N//2):
    for j in range (1, Colonne):
        if Mat[i][j] % 2 != 0:
            Pari = False
    Colonne-=1

if Pari:
    print('Tutti pari')
else:
    print('Non tutti pari')
