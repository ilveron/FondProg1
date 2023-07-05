def main():
    N = int(input())
    Binario = BinarioRicorsivo(N,'')
    print(Binario)

def BinarioRicorsivo(N, Stringa):
    if N == 0:
        return Stringa + '0'
    elif N == 1:
        return Stringa + '1'
    else:
        return BinarioRicorsivo(N//2, Stringa) + str(N%2)

main()
