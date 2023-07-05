def SommePariDispari(L, NumSommati):
    print(L)
    if len(L) > 1:
        Primo = L[0]
        Secondo = L[1]
        if NumSommati == 0 or NumSommati % 2 == 0: 
            if (Primo + Secondo) % 2 == 0: #Quindi la somma è pari
                return SommePariDispari(L[1:], NumSommati+1)
            else:
                return False
        else:
            if (Primo + Secondo) % 2 == 1: #Quindi la somma è dispari
                return SommePariDispari(L[1:], NumSommati+1)
            else:
                return False
    else:
        return True

def main():
    Tappo = 0
    N = int(input())
    L = []
    while N != Tappo:      
        L.append(N)
        N = int(input())
    print(SommePariDispari(L,0), end='')
        
    
main()
