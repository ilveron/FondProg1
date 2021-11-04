def Farfallizza(Frase):
    Risultato = ''
    for Car in Frase:
        if Car in 'aeiou':
            Risultato += Car+'f'+Car
        else:
            Risultato+=Car
    return Risultato

def InvertiParti(Farf):
    LunghezzaFarf = len(Farf)
    Mezzo = LunghezzaFarf//2
    return Farf[Mezzo:]+Farf[:Mezzo]
    

def main():
    F = input()
    Farfallizzata = Farfallizza(F)
    print(InvertiParti(Farfallizzata), end='')

main()
