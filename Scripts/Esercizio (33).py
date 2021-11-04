TriploNove = False
NumSottosequenze = 0
N = -1
NumPrecedenteUno = -2
NumPrecedenteDue = -3
while not TriploNove:
    NumPrecedenteDue = NumPrecedenteUno
    NumPrecedenteUno = N
    N = int(input())
    if N != 9:
        if N == NumPrecedenteUno == NumPrecedenteDue:
            NumSottosequenze += 1
    elif N == NumPrecedenteUno == NumPrecedenteDue:
        TriploNove = True

print(NumSottosequenze, end='')
            
        
        
    
        
    
    
