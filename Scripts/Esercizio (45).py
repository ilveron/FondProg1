N = int(input())
Tappo = -1
NumInserito = int(input())
MaxMinoriConsecutivi = 0
MinoriConsecutiviCorrenti = 0
while NumInserito != Tappo:
    if NumInserito <= N:
        MinoriConsecutiviCorrenti += 1
    else:
        MinoriConsecutiviCorrenti = 0
    if MinoriConsecutiviCorrenti > MaxMinoriConsecutivi:
            MaxMinoriConsecutivi = MinoriConsecutiviCorrenti
    NumInserito = int(input())

if MaxMinoriConsecutivi >= N:
    print('OK', end='')
else:
    print('NO', end='')
    

        
    
