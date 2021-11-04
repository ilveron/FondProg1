X = int(input())
Y = int(input())
k = X
Somma = 0

while k <= Y:
    if k % 2 == 1:
        Somma += k
    k+=1

print(Somma, end='')
