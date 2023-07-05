Carattere = input()
AlmenoUnaLettera = False

if Carattere == '.':
    print('NO', end='')
else:
    while Carattere != '.':
        if Carattere.isalpha():
            AlmenoUnaLettera = True
        Carattere = input()

    if AlmenoUnaLettera:
        print('SI', end='')
    else:
        print('NO', end='')
        
