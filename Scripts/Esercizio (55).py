from math import log2
N = int(input())
Tappo = 0
TuttePotenzeDue = True
while N != 0:
    if not float(log2(N)).is_integer():
        TuttePotenzeDue = False
    N = int(input())

if TuttePotenzeDue:
    print('SI', end='')
else:
    print('NO', end='')
