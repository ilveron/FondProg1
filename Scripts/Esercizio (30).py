N = int(input())
Primo = bool(1)

for k in range(2,(N//2)+1):
    if N % k == 0:
        Primo = bool(0)
        break;

if Primo:
    print('SI', end='')
else:
    print('NO', end='')
