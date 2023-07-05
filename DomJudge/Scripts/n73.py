def CreaNuovoN(N):
    NumConsecutivi = 1
    CifraPrecedente = int(N[0])
    NuovoN = str()
    
    for k in range(1,len(N)):
        Cifra = int(N[k])
        if Cifra == CifraPrecedente:
            NumConsecutivi+=1
        else:
            NuovoN += str(NumConsecutivi)
            NuovoN += str(CifraPrecedente)
            NumConsecutivi = 1
        CifraPrecedente = Cifra
    NuovoN+=str(NumConsecutivi)
    NuovoN+=str(CifraPrecedente)
    return NuovoN

def StampaNuovoN(NuovoN):
    print(NuovoN, end=' ')
    print(len(NuovoN), end='')
    
def main():
    N = input()
    NuovoN = CreaNuovoN(N)   
    StampaNuovoN(NuovoN)

main()
