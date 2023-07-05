A = int(input())
B = int(input())
C = int(input())

if (A < (B+C) and B < (A+C) and C < (A+B)):
    Equilatero = (A==B and B==C)
    Isoscele = (A==B and B!=C) or (A==C and A!=B) or (B==C and B!=A)
    if Equilatero:
        print('TRIANGOLO EQUILATERO', end='')
    elif Isoscele:
        print('TRIANGOLO ISOSCELE', end='')
    else:
        print('TRIANGOLO SCALENO', end='')
else:
    print('NO', end='')
