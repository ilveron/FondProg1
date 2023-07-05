from random import randint

def LunghezzaUguale(P1, P2):
    if len(P1) == len(P2):
        return True
    else:
        return False
    
def Anagramma(P1, P2):
    for Elemento in P1:
        if Elemento in P2:
            P2.remove(Elemento)
        else:
            return False
        
    if P2 == []:
        return True
    else:
        return False
    
def CreaAnagramma(P, LunghezzaIniziale):
    Nuovo = ''
    for k in range(LunghezzaIniziale):
        LenP = len(P)
        Elemento = P[randint(0, LenP-1)]
        P.remove(Elemento)
        Nuovo += Elemento
    return Nuovo
        
    
    

def main():
    P1 = input('Inserisci la prima parola: ')
    P2 = input('Inserisci la seconda parola: ')
    if LunghezzaUguale(P1, P2):
        if Anagramma(list(P1), list(P2)):
            print("Le due parole sono l'una l'anagramma dell'altra", end='')
        else:
            print("Le due parole NON sono l'una l'anagramma dell'altra")
            NuovoAnagramma = CreaAnagramma(list(P1), len(P1))
            print("Eccoti un'anagramma creato con la prima parola: ", NuovoAnagramma, end='')
    else:
        print("Attenzione, le parole sono di lunghezza diversa, riavvia il programma e riprova", end='')

main()
