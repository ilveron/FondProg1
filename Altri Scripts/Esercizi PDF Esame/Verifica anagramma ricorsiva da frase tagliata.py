def CreaF1(F, N):
    F1 = ''
    for k in range(N):
        if F[k].isalpha():
            F1+=F[k]
    return F1

def CreaF2(F,N):
    F2 = ''
    for k in range(N, len(F)):
        if F[k].isalpha():
            F2+=F[k]
    return F2

def Verifica(F1, F2):
    if F1 == []:
        return True
    else:
        PrimoCarattere = F1[0]
        if PrimoCarattere in F2:
            F1.remove(PrimoCarattere)
            return Verifica(F1, F2)
        else:
            return False
    

def main():
    N = int(input('Inserisci un numero\n'))
    F = input('Inserisci la frase:\n')
    F1 = CreaF1(F,N)
    F2 = CreaF2(F,N)
    
    if len(F1) != len(F2) or not Verifica(list(F1),list(F2)):
        print('NO', end='')
    else:
        print('SI', end='')
                   
main()
