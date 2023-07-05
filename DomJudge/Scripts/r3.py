def CostruisciMatrice(Mat, N):    
    for i in range(N):        
        Riga = []
        for j in range(N):
            Riga.append(int(input()))
        Mat.append(Riga)

def Ricorsivo(Mat,i):    
    if i>len(Mat)-1:
        return 0
    else:
        return (Mat[i][len(Mat)-1-i])+Ricorsivo(Mat,i+1)
        

def main():
    N = int(input())
    Mat = []
    CostruisciMatrice(Mat, N)
    print(Ricorsivo(Mat,0),';',Ricorsivo(Mat,0), sep='', end='')

main()
