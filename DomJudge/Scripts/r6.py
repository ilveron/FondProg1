def CostruisciMatrice(Mat, N):  
    for i in range(N):
        Riga = []
        for j in range(N):
            Riga.append(int(input()))
        Mat.append(Riga)
        
def ControlloVert(Mat,RigaDiv,ColDiv, Somma):    
    for i in range(RigaDiv):
        Somma+=Mat[i][ColDiv]
    return Somma

def ControlloOriz(Mat, RigaDiv, ColDiv, Somma):
    for j in range(ColDiv+1, len(Mat)):
        Somma+=Mat[RigaDiv][j]
    return Somma

def ControlloL(Mat, RigaDiv, ColDiv):
    if RigaDiv == 0:
        return True
    else:
        Verticale = ControlloVert(Mat, RigaDiv, ColDiv, 0)     
        Div = Mat[RigaDiv][ColDiv]
        Somma = ControlloOriz(Mat, RigaDiv, ColDiv, Verticale)+Div
        if Somma%Div == 0:
            return ControlloL(Mat, RigaDiv-1, ColDiv+1)
        else:
            return False
                
def main():
    N = int(input())
    if N>=2:
        Mat = []
        CostruisciMatrice(Mat, N)
        RigaDivisore = N-1
        ColonnaDivisore=0
        if ControlloL(Mat, len(Mat)-1, 0):
            print('SI', end='')
        else:
            print('NO', end='')
            
main()
