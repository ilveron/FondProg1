def CalcolaMedia(Valori):
    Somma = sum(Valori)
    return Somma//len(Valori)

def CostruisciMaggioriUguali(Media, Valori):
    MaggioriUgualiMedia = []
    for Elemento in Valori:
        if Elemento >= Media:
            MaggioriUgualiMedia.append(Elemento)
    return MaggioriUgualiMedia
    
    
def main():
    Tappo = -50
    Valori = []
    N = int(input('Inserisci un valore (tappo -50):\n'))
    while N != Tappo:
        Valori.append(N)
        N = int(input('Inserisci un valore (tappo -50):\n'))
    if Valori != []:
        Media = CalcolaMedia(Valori)
        MaggioriUgualiMedia = CostruisciMaggioriUguali(Media, Valori)
        print(MaggioriUgualiMedia)
        print(min(MaggioriUgualiMedia), end='')
    else:
        print('0', end='')
        
    
main()
