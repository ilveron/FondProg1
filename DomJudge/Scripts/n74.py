def CalcolaAsterischi(N):
    Totali = 0
    for k in range(1, N+1):
        if k == N:
            TriangoloSup = Totali
            
        Totali += k+(k-1)
        
    Totali += TriangoloSup
    
    return Totali
        

def main():
    N = int(input())
    Totali = CalcolaAsterischi(N)
    print(Totali, end='')
    
main()
