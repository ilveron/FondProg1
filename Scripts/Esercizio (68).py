def GestisciRisposta(Matricola, Date, Esatte):
    Voto = 0
    for k in range(len(Date)):
        if Date[k] == Esatte[k]:
            Voto += 2
        elif Date[k] != 'X' and Date[k] != Esatte[k]:
            Voto -= 1
    print(Matricola, Voto)
            

def main():
    Esatte = input()
    for k in range(90):
        Matricola = input()
        Date = input()        
        GestisciRisposta(Matricola,Date,Esatte)
        
main()        
