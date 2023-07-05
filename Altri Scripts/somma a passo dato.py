#Presi A e B stampa la somma dei numeri compresi tra loro a passo 2

A = int(input())
B = int(input())
P = int(input())

Somma = 0

for k in range (A, B+1, P):
    Somma += k

print(Somma, end='')
