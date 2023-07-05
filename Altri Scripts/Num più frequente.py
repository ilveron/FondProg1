Frequenza = [0,0,0,0,0,0,0,0,0,0]

for k in range(100):
    NumInserito = int(input('Inserisci un numero da 1 a 10:'))
    Frequenza[NumInserito-1]+=1

print(Frequenza[max(Frequenza)])
    
