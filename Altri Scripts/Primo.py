#Verifica se un numero preso da input è primo

N = int(input())
Primo = True

for k in range (2, N//2+1):
    if N%k == 0:
        Primo = False

if Primo:
    print("E' primo", end='')
else:
    print("Non è primo", end='')
