Fumatori = [0, 0, 0, 0, 0]
FumatoriPieno = False
NonFumatori = [0, 0, 0, 0, 0]
NonFumatoriPieno = False

while (0 in Fumatori) or (0 in NonFumatori):
    Scelta = input("Digitare 1 per fumatori o 2 per non fumatori:")
    if Scelta == '1':
        if not FumatoriPieno:
            PrimoPostoLibero = Fumatori.index(0)
            Fumatori[PrimoPostoLibero] = 1
            print("Reparto fumatori, posto", PrimoPostoLibero+1)
            if 0 not in Fumatori:
                FumatoriPieno = True
        else:
            Ripiego = input("Reparto scelto al completo. Si desidera un posto nell'altro reparto (S/N)?")
            if Ripiego == 'S':
                PrimoPostoLibero = NonFumatori.index(0)
                NonFumatori[PrimoPostoLibero] = 1
                print("Reparto NON fumatori, posto", PrimoPostoLibero+1+5)
            else:
                print("Il prossimo volo parte tra 3 ore")
    else:
        if not NonFumatoriPieno:
            PrimoPostoLibero = NonFumatori.index(0)
            NonFumatori[PrimoPostoLibero] = 1
            print("Reparto NON fumatori, posto", PrimoPostoLibero+1+5)
            if 0 not in NonFumatori:
                NonFumatoriPieno = True
        else:
            Ripiego = input("Reparto scelto al completo. Si desidera un posto nell'altro reparto (S/N)?")
            if Ripiego == 'S':
                PrimoPostoLibero = Fumatori.index(0)
                Fumatori[PrimoPostoLibero] = 1
                print("Reparto fumatori, posto", PrimoPostoLibero+1)
            else:
                print("Il prossimo volo parte tra 3 ore")
                
            
            


