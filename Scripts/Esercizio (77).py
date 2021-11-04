def InvertiLista(L, Invertita):
    if L == []:
        return Invertita
    else:
        Invertita+=str(L[len(L)-1])
        return InvertiLista(L[:len(L)-1], Invertita)

def main():
    N = int(input())
    L = []
    for k in range(N):
        L.append(int(input()))
    Invertita = InvertiLista(L, '')
    print(Invertita, end='')
    
main() 
