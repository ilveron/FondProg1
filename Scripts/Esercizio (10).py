A = int(input())
while True:
    B = int(input())
    if B != 0:
        break;

Somma = A+B
Diff = A-B
Molt = A*B
Quoz = int(A/B)
Resto = A%B

print('Somma:', Somma)
print('Differenza:', Diff)
print('Moltiplicazione:', Molt)
print('Quoziente:', Quoz)
print('Resto:', Resto, end='')
