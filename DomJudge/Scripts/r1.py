def Fibonacci(n):
   if n == 0:
       return 2
   else:
       return(3*Fibonacci(n-1)*(n+1))

def main():
    n = int(input())

    print(Fibonacci(n), end='')

main()
