def main ():
    PRIMAPAROLA= input()
    SECONDAPAROLA= input()
    if len(PRIMAPAROLA)==len(SECONDAPAROLA):
        anagramma= CheckAnagramma (PRIMAPAROLA,SECONDAPAROLA)
        if anagramma==True:
            print ('SI',end="")
        else:
            print (nuovaparola(PRIMAPAROLA))
    else:
        print (nuovaparola(PRIMAPAROLA))

def CheckAnagramma(PRIMAPAROLA,SECONDAPAROLA):
    ListaUno= paroleinlista (PRIMAPAROLA)
    ListaDue= paroleinlista (SECONDAPAROLA)
    for i in range (len(ListaUno)):
        for j in range (len(ListaDue)):
            if ListaUno[i]==ListaDue[j]:
                ListaDue.pop(j)
                break
    if len(ListaDue)==0:
        return True
    else:
        return False

def paroleinlista (parola):
    Lista=[]
    for i in range (len(parola)):
        Lista.append (parola[i])

    return Lista

def nuovaparola(PRIMAPAROLA):
    from random import randint
    Lista= paroleinlista(PRIMAPAROLA)
    nuovaparola=''
    while len(Lista)>0:
        i=randint (0,len(Lista)-1)
        nuovaparola+=Lista[i]
        Lista.pop (i)
    return nuovaparola

main ()
