N = int(input())
Ok = 0

while N != 0:
    if N % 2 != 0 and N % 3 == 0:
        Ok+=1
    N = int(input())
print(Ok, end='')
