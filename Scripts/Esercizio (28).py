N=input()
k = len(N)-1
Ninv = ''

while k >= 0:
    Ninv+=N[k]
    k-=1

print(int(N)-int(Ninv), end='')
