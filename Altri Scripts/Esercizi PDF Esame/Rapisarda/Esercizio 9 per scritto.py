def main ():
    Frase1=input('Inserisci la prima frase:')
    Frase2=input('Inserisci la seconda frase:')
    FL1=FraseListata(Frase1)
    FL2=FraseListata(Frase2)
    check=CheckFurbetti(FL1,FL2)
    print (len(check), check)


def FraseListata (FRASE):
    Lista=[]
    parola=''
    for i in range (len(FRASE)):
        if FRASE[i]!=' ' and i<len(FRASE)-1:
            parola+=FRASE[i]
        elif FRASE[i]==' ':
            Lista.append (parola)
            parola=''
        elif FRASE[i]!=' ' and i==len(FRASE)-1:
            parola+=FRASE[i]
            Lista.append(parola)

    return Lista

def CheckFurbetti(lista1,lista2):
    lista=[]
    if len(lista1)>=len(lista2):
        for i in range (len(lista1)):
            if lista2.count (lista1[i])>=1:
                lista.append (lista1[i])
    else:
        for i in range (len(lista2)):
            if lista1.count (lista2[i])>=1:
                lista.append (lista2[i])

    return lista

main()
