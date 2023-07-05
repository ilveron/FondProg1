#Matrice diagonale

Mat =[
        [1, 0, 0, 0],
        [0, -2, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 81]
     ]

Quadrata = True

for i in range (len(Mat)):
    for j in range (len(Mat)):
        if Mat[i][j] != 0 and i != j:
            Quadrata = False

if Quadrata:
    print('Matrice quadrata')
else:
    print('Matrice NON quadrata')
            
