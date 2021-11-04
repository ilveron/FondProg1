X = int(input())
N = int(input())
OccorrenzeZeroCorrenti = 0
OccorrenzeZeroMax = 0
while N != -1:
    if N == 0:
        OccorrenzeZeroCorrenti += 1
    else:
        OccorrenzeZeroCorrenti = 0

    N = int(input())
    
    if OccorrenzeZeroCorrenti > OccorrenzeZeroMax:
            OccorrenzeZeroMax = OccorrenzeZeroCorrenti

if OccorrenzeZeroMax >= X:
    print('OK', end='')
else:
    print('NO', end='')
    
