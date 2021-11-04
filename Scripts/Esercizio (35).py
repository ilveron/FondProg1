Tappo = 0
NumPrecedente = -1
N = int(input())
Verificate = False

while N != Tappo:       
    if NumPrecedente == -1:
        NumPrecedente = N
        N = int(input())          
    else:
        if (N%2 == 0 and NumPrecedente%2 == 0) or ((N+NumPrecedente) % N == 0 or (N+NumPrecedente) % NumPrecedente == 0): 
            Verificate = True
        NumPrecedente = N
        N = int(input())    
if Verificate:
    print('SI', end='')
else:
    print('NO', end='')
            
        
        
        
