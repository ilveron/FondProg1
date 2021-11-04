def StampaMaggioreMinore(L):
    Minore = L[0]
    Maggiore = L[0]
    
    for k in range(1, len(L)):
        if L[k] < Minore:
            Minore = L[k]
        if L[k] > Maggiore:
            Maggiore = L[k]
    print(Maggiore+Minore, end='')
        
            
def main():
    S = input()
    N = int(input())
    L = []
    Presente = False
    for k in range (N):
        L.append(input())

    for i in range(len(L)-1):
        for j in range(i, len(L)):
            if L[i]+L[j] == S or L[j]+L[i] == S:
                Presente = True
    if Presente:
        print('OK', end='')
    else:
        StampaMaggioreMinore(L)

main()
