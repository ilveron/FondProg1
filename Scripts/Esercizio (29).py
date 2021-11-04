N = input()
DiverseDaZero = bool(1)

for k in range(0,len(N)):
    if N[k] == '0':
        DiverseDaZero = bool(0)
        break

if DiverseDaZero:
    print('SI', end='')
else:
    print('NO', end='')
    
