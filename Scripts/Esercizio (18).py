Anno = int(input())

if Anno%4 == 0:
    if Anno%100 == 0:
        if Anno%400 != 0:
            print('NON BISESTILE', end='')
        else:
            print('BISESTILE', end='')
    else:
        print('BISESTILE', end='')
else:
    print('NON BISESTILE', end='')

    
