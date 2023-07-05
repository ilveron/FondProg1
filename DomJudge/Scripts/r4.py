def main():
    X = int(input())
    N = int(input())
    L = []
    for k in range(N):
        L.append(int(input()))
    print(Ricerca(X,L,0),end='')
                

def Ricerca(X, L, Somma):
    C=0
    for k in range(len(L)):
        if L[k] == X:
            L[k] = 0                
            C+=1
    if C == 0:
        return 0
    else:
        Somma=C
        return(Somma+Ricerca(C,L,Somma))

main()
