N= int(input("Di quanti numeri in totale vuoi effettuare la somma?\n"))
cont = 0
SommaPositivi = 0
SommaNegativi = 0

if N != 0:
    while cont < N:
        DaInserire = int(input(str(cont+1)+'° ' + 'numero: '))
        
        if DaInserire < 0:
            SommaNegativi += DaInserire
        else:
            SommaPositivi += DaInserire
            
        cont+=1
        
    print('La somma dei numeri positivi è:', SommaPositivi)
    print('La somma dei numeri negativi è:', SommaNegativi)
else:
    print('La somma di 0 numeri è: 0', end='')


