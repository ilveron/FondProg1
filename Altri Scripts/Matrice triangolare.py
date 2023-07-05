#Matrice triangolare superiore

Mat =[
        [1, 0, 3, 4],
        [0, -2, 5, 9],
        [0, 0, 0, 1],
        [0, 0, 0, 81]
     ]

Triangolare = True

for i in range (1,len(Mat)):
    for j in range (i):
        if Mat[i][j] != 0 and i > j:
            Triangolare = False    


if Triangolare:
    print('Matrice triangolare superiore')
else:
    print('Matrice NON triangolare superiore')
            
