Mese = int(input())

if Mese > 0 and Mese <= 3:
    if Mese == 3:
        Giorno = int(input())        
        if(Giorno < 1 or Giorno > 20):
            print('PRIMAVERA', end='')
        else:
            print('INVERNO', end='')    
    else:
        print('INVERNO', end='')
        
elif Mese >= 4 and Mese <= 6:
    if Mese == 6:
        Giorno = int(input())   
        if(Giorno < 1 or Giorno > 20):
            print('ESTATE', end='')
        else:
            print('PRIMAVERA', end='')
    else:
        print('PRIMAVERA', end='')
        
elif Mese >= 7 and Mese <= 9:
    if Mese == 9:
        Giorno = int(input())    
        if(Giorno < 1 or Giorno > 20):
            print('AUTUNNO', end='')
        else:
            print('ESTATE', end='')    
        
    else:
        print('ESTATE', end='')
        
elif Mese >= 10 and Mese <= 12:
    if Mese == 12:
        Giorno = int(input())    
        if(Giorno < 1 or Giorno > 20):
            print('INVERNO', end='')
        else:
            print('AUTUNNO', end='')
    else:
        print('AUTUNNO', end='')

else:
    print('MESE NON VALIDO', end='')

    
