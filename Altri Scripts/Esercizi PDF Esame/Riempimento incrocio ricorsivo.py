def RiempiIncrocio(A,B,C):
    if B == []:
        return C
    else:
        C += A[0]+B[len(B)-1]
        return RiempiIncrocio(A[1:],B[:len(B)-1],C)

def main():
    A = list(input('Inserire A'))
    B = list(input('Inserire B'))
    if(len(A)==len(B)):
        print(RiempiIncrocio(A,B,[]))
    else:
        print('Non è possibile effettuare incrocio di liste di dimensione differenti')
    
main()        
    
        
