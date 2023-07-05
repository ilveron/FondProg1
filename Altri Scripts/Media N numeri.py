N= int(input("Di quanti numeri (interi) vuoi effettuare la media?\n"))
cont = 1
Somma = 0

if N != 0:
    while cont <= N:
        Somma += int(input(str(cont)+'° ' + 'numero (intero): ')) #Aggiungo all'accumulatore il numero inserito
        cont+=1
    
    print('La media dei', N, 'numeri inseriti è:', Somma/N, end='')
else:
    print('La media di 0 numeri è: 0', end='')


