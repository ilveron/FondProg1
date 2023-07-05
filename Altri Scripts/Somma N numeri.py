N= int(input("Di quanti numeri vuoi effettuare la somma?\n"))
cont = 1
Somma = 0

if N != 0:
    while cont <= N:
        Somma += int(input(str(cont)+'° ' + 'numero: ')) #Aggiungo all'accumulatore il numero inserito
        cont+=1
    print('La somma dei', N, 'numeri è:', Somma, end='')
else:
    print('La somma di 0 numeri è: 0', end='')


