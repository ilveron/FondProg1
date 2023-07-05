from random import *
VittorieGiocatore = 0
VittorieCpu = 0
seed(0)

while VittorieCpu != 3 and VittorieGiocatore != 3:
    #(1: sasso, 2: carta, 3: forbice)
    MossaGiocatore = int(input("Inserisci la giocata del primo giocatore (1: sasso, 2: carta, 3: forbice):"))
    while MossaGiocatore not in range(1,4):
        MossaGiocatore = int(input("Inserisci la giocata del primo giocatore (1: sasso, 2: carta, 3: forbice):"))
    
    MossaCpu = randint(1,3)
    if MossaGiocatore == 1:
        print('hai giocato sasso')
        if MossaCpu == 1:
            print('il PC ha giocato sasso')
            print('Pari:')
        elif MossaCpu == 2:
            print('il PC ha giocato carta')
            print('Vince il PC:')
            VittorieCpu+=1
        else:
            print('il PC ha giocato forbice')
            print('Vinci tu:')
            VittorieGiocatore+=1
    elif MossaGiocatore == 2:
        print('hai giocato carta')
        if MossaCpu == 1:
            print('il PC ha giocato sasso')
            print('Vinci tu:')
            VittorieGiocatore+=1
        elif MossaCpu == 2:
            print('il PC ha giocato carta')
            print('Pari:')            
        else:
            print('il PC ha giocato forbice')
            print('Vince il PC:')
            VittorieCpu+=1
    else:
        print('hai giocato forbice')
        if MossaCpu == 1:
            print('il PC ha giocato sasso')
            print('Vince il PC:')
            VittorieCpu+=1
        elif MossaCpu == 2:
            print('il PC ha giocato carta')
            print('Vinci tu:')
            VittorieGiocatore+=1
        else:
            print('il PC ha giocato forbice')
            print('Pari:')      

    print(VittorieGiocatore, '-', VittorieCpu, sep='')

if VittorieGiocatore > VittorieCpu:
    print("Hai vinto la sfida!")
else:
    print("Il PC ha vinto la sfida!")
    
 
                            
                            
        
