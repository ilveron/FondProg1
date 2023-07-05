Tappo = '.'
A = []
B = []
Disgiunti = True
PrimoElementoUguale = ''

for k in range(2):
    Car = input()
    if k == 0:        
        while Car != Tappo:
            A.append(Car)
            Car = input()
    else:
        while Car != Tappo:
            B.append(Car)
            Car = input()

for ElementoA in A:
    if PrimoElementoUguale == '':
        for ElementoB in B:
            if ElementoA == ElementoB:
                PrimoElementoUguale = ElementoA
                Disgiunti = False
                break
    else:
        break

if Disgiunti:
    print('DISGIUNTE', end='')
else:
    print(PrimoElementoUguale, end='')
            
            
