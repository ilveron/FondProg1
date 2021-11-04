def MCD(A,B):
    r = A%B
    if r == 0:
        return B
    else:
        return MCD(B,r)

def main():
    A = int(input())
    B = int(input())
    if A > B:
        print(MCD(A,B), end='')
        
main()
