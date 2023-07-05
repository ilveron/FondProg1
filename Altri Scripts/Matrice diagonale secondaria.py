#Matrice

Mat =[
        [1, 0, 3, 1],
        [0, -2, 0, 9],
        [0, 8, 0, 1],
        [24, 0, 0, 81]
     ]

Somma = 0
N = 4

for i in range (len(Mat)):
    Somma += Mat[i][(N-1)-i]

print(Somma)
            
