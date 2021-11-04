Tappo = '.'
CaratterePrecedente = ''
Carattere = input()
NumSottosequenze = 0

while Carattere != Tappo:    
    if CaratterePrecedente == '':
        CaratterePrecedente = Carattere
    if not ((CaratterePrecedente in 'aeiou' and Carattere not in 'aeiou') or (CaratterePrecedente not in 'aeiou' and Carattere in 'aeiou')):
        NumSottosequenze+=1
    CaratterePrecedente = Carattere
    Carattere = input() 
        
print(NumSottosequenze, end='')
