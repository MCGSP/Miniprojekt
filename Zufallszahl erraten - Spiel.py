#Zufallszahl erraten - Spiel

import random
zahl = random.randint(1, 100)
versuch = int(input("Ich habe mir eine Zahl von 1 bis 100 ausgedacht. Du hast 10 Versuche, um sie zu erraten: "))
versuchsanzahl = 1
while versuchsanzahl < 10:
    if versuch < zahl:
        versuch = int(input("Zu niedrig, versuch es nochmal: "))
        versuchsanzahl = versuchsanzahl + 1
    if versuch > zahl:
        versuch = int(input("Zu hoch, versuch es nochmal: "))
        versuchsanzahl = versuchsanzahl + 1
    if versuch == zahl:
        print("Du hast meine Zahl in " + str(versuchsanzahl) + " Versuchen erraten!")
        
print("Du hast keine Versuche mehr übrig.")