N = int(input())
Candidato1 = 0
Candidato2 = 0
Candidato3 = 0
if N != 0:
    while N != 0:
        if N == 1:
            Candidato1 += 1
        elif N == 2:
            Candidato2 += 1
        else:
            Candidato3 += 1
        N = int(input())


    VotiTotali = Candidato1+Candidato2+Candidato3
    PercCand1 = round(Candidato1/VotiTotali*100, 1)
    PercCand2 = round(Candidato2/VotiTotali*100, 1)
    PercCand3 = round(Candidato3/VotiTotali*100, 1)

    print(1, Candidato1, PercCand1)
    print(2, Candidato2, PercCand2)
    print(3, Candidato3, PercCand3)

    if (PercCand1 > 50 or PercCand2 > 50 or PercCand3 > 50):
        if PercCand1 > PercCand2:
            if PercCand1 > PercCand3:
                print('VINCE 1', end='')
            else:
                print('VINCE 3', end='')
        elif PercCand2 > PercCand3:
            print('VINCE 2', end='')
        else:
            print('VINCE 3', end='')
    else:
        print('BALLOTTAGGIO', end='')
else:
    print('BALLOTTAGGIO', end='')


