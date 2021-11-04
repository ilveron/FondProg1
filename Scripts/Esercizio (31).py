X = int(input())
Y = int(input())

XPrimo = bool(1)
YPrimo = bool(1)

for k in range(2,(X//2)+1):
    if X % k == 0:
        XPrimo = bool(0)
        break;

for k in range(2,(Y//2)+1):
    if Y % k == 0:
        YPrimo = bool(0)
        break;
    
if XPrimo and YPrimo:
    if abs(X-Y) == 2:
        print('gemelli', end='')
    else:
        print('non gemelli', end='')
else:
    print('non entrambi primi', end='')
