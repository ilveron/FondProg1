CostoMateriale = int(input())
OreLavoro = int(input())
LimiteMinimo = 100

Spesa = CostoMateriale+(40*OreLavoro)

if Spesa < 100:
    print(LimiteMinimo, end='')
else:
    print(Spesa, end='')
    
