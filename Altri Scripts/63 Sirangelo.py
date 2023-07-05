def main():
    N = int(input())
    potenza = 0
    print(PotenzaDueAlla(N, potenza))

def PotenzaDueAlla(esp,potenza):
    if esp == 0:
        return potenza + 1
    else:
        return 2*PotenzaDueAlla(esp-1,potenza)
    
main()
