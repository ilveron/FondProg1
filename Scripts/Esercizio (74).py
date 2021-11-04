def VerificaRicorsiva(Lista, Estratta):
    if len(Lista) == len(Estratta):
        if Lista == Estratta:
            return True
        else:
            return False
    else:
        Estratta.append(Lista[0])
        return VerificaRicorsiva(Lista[1:], Estratta)
        
    

def main():
    N = int(input())
    if N % 2 == 0:       
        L = []
        for k in range(N):
            L.append(int(input()))
        if VerificaRicorsiva(L,[]):
            print('SI', end='')
        else:
            print('NO', end='')
        
main()
