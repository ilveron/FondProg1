def InizializzaMatrice(Mat):
     for k in range(10):
        Mat.append([0,0,0,0,0,0,0,0,0,0])

def InizializzaLista(L, X):
    for k in range(1,X+1):
        L.append(k)


def SommaDiagSec(Mat):
    Somma = 0
    for i in range(len(Mat)):
        Somma+=Mat[i][len(Mat)-1-i]
    return Somma
    
def main():
    X = int(input())
    L = []
    Mat = []
    InizializzaMatrice(Mat)
    InizializzaLista(L, X)

    Pos = 0
    
    for i in range(10):
        for j in range(10):
            Mat[i][j] = L[Pos]
            if Pos == len(L)-1:
                Pos = 0
            else:
                Pos+=1
                
    print(SommaDiagSec(Mat), end='')

main()
