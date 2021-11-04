DoppioZero = False
N = -1
Somma = 0
Somme = []

while not DoppioZero:
    NumPrecedente = N 
    N = int(input())     
    
    if N != 0:
        Somma += N
    else:        
        if NumPrecedente != 0:            
            Somme.append(Somma)                      
        else:
            DoppioZero = True
        Somma = 0
    
for k in range (0,len(Somme)):
    print(Somme[k])   
    
