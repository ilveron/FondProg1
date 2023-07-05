Lista = []
StringaElementiOk = ''
ElementiDaFareMedia = []
for k in range(0,100):
    Lista.append(int(input()))

for Elemento in Lista:
    if Elemento < -50 or Elemento > 50:
        StringaElementiOk += str(Elemento)
    else:
        ElementiDaFareMedia.append(Elemento)

if StringaElementiOk != '':
    print(StringaElementiOk)
else:
    print('VUOTO1')

if len(ElementiDaFareMedia) != 0:
    print(round(sum(ElementiDaFareMedia)/len(ElementiDaFareMedia), 6), end='')
else:
    print('VUOTO2', end='')
    
