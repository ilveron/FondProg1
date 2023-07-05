def CreaElencoMail(Elenco):
    Tappo = '.'
    Mail = input("Inserisci la mail: (per terminare input scrivere solo '.')\n")
    while Mail != Tappo:
        Elenco.append(Mail)
        Mail = input("Inserisci la mail: (per terminare input scrivere solo '.')\n")
    
def ContaParoleProibite(Elenco, ParoleProibite):
    N = 0
    for ParolaProibita in ParoleProibite:
        for Mail in Elenco:
            if ParolaProibita in Mail:
                N+=1
    return N            
    

def main():
    Elenco = []
    ParoleProibite = ('amore', 'tesoro', 'cucciolotto', 'trottolino')
    CreaElencoMail(Elenco)
    NumParoleProibite = ContaParoleProibite(Elenco, ParoleProibite)
    if NumParoleProibite > 0:       
        print('Mi dispiace Renata... Tuo marito ha usato almeno una delle parole proibite in', NumParoleProibite, 'delle sue mail')
    else:
        print("Renata, tuo marito è un modello, non c'è nessuna mail contenente parole proibite... A meno che...")
        

main()    
    
    
