def EliminaLetterePresenti(F, Alfabeto):
    for Lettera in F:
        if Lettera in Alfabeto:
            Alfabeto.remove(Lettera)

def main():
    F = input()
    Alfabeto = ['a','b','c','d','e','f','g','h','i','j',
                'k','l','m','n','o','p','q','r','s','t',
                'u','v','w','x','y','z']
    EliminaLetterePresenti(F, Alfabeto)
    if len(Alfabeto)==0:
        print('SI', end='')
    else:
        print('NO', end='')
    
main()
