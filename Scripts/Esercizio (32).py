N = int(input())
CifreGiustapposte = ''
if N != -1:
    TutteDecimali = bool(1)
    while N != -1:
        if N < 10 and N >= 0:
            CifreGiustapposte += str(N)
        else:
            TutteDecimali = bool(0)
        N = int(input())

    if TutteDecimali:
        print(CifreGiustapposte)
        if int(CifreGiustapposte) % 3 == 0:
            print('SI', end='')
        else:
            print('NO', end='')
    else:
        print('ERRORE', end='')
else:
    print('VUOTO', end='')
    
        
    
