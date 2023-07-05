Chiamate = int(input())

if Chiamate <= 80:
    Bolletta = 5
elif Chiamate <= 140:
    Bolletta = round(5 + 0.1*(Chiamate-80),3)
elif Chiamate <= 190:
    Bolletta = round(5 + 0.1*(60) + 0.07*(Chiamate-140), 3)
else:
    Bolletta = round(5 + 0.1*(60) + 0.07*(50) + 0.05*(Chiamate-190),3)
    
print(Bolletta, end='')
