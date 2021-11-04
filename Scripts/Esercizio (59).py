def SelectionSort(Lista):
    for i in range(0,len(Lista)-1):
        minimo = i
        for j in range (i+1, len(Lista)):
            if Lista[j] < Lista[minimo]:
                minimo = j
        Copia = Lista[i]
        Lista[i] = Lista[minimo]
        Lista[minimo] = Copia

def GeneraNmin(Lista):
    ListaInStringa = ''
    for Elemento in Lista:
        ListaInStringa += Elemento
    return int(ListaInStringa)

def GeneraNmax(Lista):
    ListaInStringa = ''
    for k in range (len(Lista)-1, -1, -1):
        ListaInStringa += Lista[k]
    return int(ListaInStringa)

def main():
    N = input()
    ListaN = list(N)
    SelectionSort(ListaN)
    Nmin = GeneraNmin(ListaN)
    Nmax = GeneraNmax(ListaN)
    print(Nmax-Nmin, end='')
    

main()

