N = int(input())
Mat = []
SommaCroce = 0
SommaRestanti = 0

for i in range(N):
    Riga = []
    for j in range(N):
        Riga.append(int(input()))
    Mat.append(Riga)

for i in range(N):
    for j in range(N):
        if i == (N // 2) or j == (N //2):
            SommaCroce += Mat[i][j]
        else:
            SommaRestanti += Mat[i][j]

if SommaCroce > SommaRestanti:
    print('OK', end='')
else:
    print('NO', end='')
        
    
