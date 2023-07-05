def main ():
    n=int(input())
    Lista=[]
    while n!=(-1):
        Lista.append(n)
        n=int(input('inserire -1 per interrompere'))
    booleana=True
    if (Lista[0]+Lista[1])%2==0:
        booleana=True
    else:
        booleana=False
    Proprieta= check (Lista,1,booleana)
    if Proprieta==True:
        print ('SI')
    else:
        print ('NO')

def check (Lista,i,booleana):
    proprieta=True
    if booleana==True and i<=len(Lista)-2:
        if (Lista[i]+Lista[i+1])%2!=0:
            booleana=False
            return check (Lista,i+1,booleana)
        else:
            proprieta=False
            return proprieta
    elif booleana==False and i<=len(Lista)-2:
        if (Lista[i]+Lista[i+1])%2==0:
            booleana=True
            return check (Lista,i+1,booleana)
        else:
            proprieta=False
            return proprieta
    elif i==len(Lista)-1:
        return proprieta

main()
