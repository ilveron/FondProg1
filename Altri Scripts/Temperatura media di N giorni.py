from random import randint
TemperatureGiorni = []
NumeroGiorni = int(input('Inserisci qui il numero dei giorni: '))
SommaTemperature = 0

for k in range(0, NumeroGiorni):
    TemperaturaOdierna = randint(-25, 45)
    TemperatureGiorni.append(TemperaturaOdierna)
    SommaTemperature += TemperaturaOdierna

TemperaturaMedia = SommaTemperature // len(TemperatureGiorni)
print('La temperatura media equivale a ', TemperaturaMedia, '°C.', sep='')

for k in range(0, NumeroGiorni):
    if TemperatureGiorni[k] > TemperaturaMedia:
        print('Giorno ', k+1, ': ', TemperatureGiorni[k])

