def main ():
    PAROLA1=input('Inserisci la prima parola:')
    PAROLA2=input('Inserisci la seconda parola:')
    if len(PAROLA1)==len(PAROLA2):
        parolina=''
        NUOVAPAROLA= FUUUSIOOONEEEE_GOKU_DOCET (PAROLA1,PAROLA2,0,parolina)
        print (NUOVAPAROLA)
    else:
        print ('False')
        
def FUUUSIOOONEEEE_GOKU_DOCET (parolaA,parolaB,i,new):
    if i<len(parolaA):
        new+=parolaA[i]
        new+=parolaB[len(parolaA)-1-i]
        return FUUUSIOOONEEEE_GOKU_DOCET (parolaA,parolaB,i+1,new)
    else:
        return new

main()
