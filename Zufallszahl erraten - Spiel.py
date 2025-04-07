#Zufallszahl erraten - Spiel

import random
zahl = random.randint(1, 100)
versuch = int(input("Ich habe mir eine Zahl von 1 bis 100 ausgedacht. Du hast 10 Versuche, um sie zu erraten: "))
versuchsanzahl = 9
while versuch < zahl:
    versuch = int(input("Zu niedrig, versuch es nochmal: "))
    versuchsanzahl = versuchsanzahl - 1
    if versuchsanzahl == 0:
        print("Du hast keine Versuche mehr übrig.")
    
while versuch > zahl:
    versuch = int(input("Zu hoch, versuch es nochmal: "))
    versuchsanzahl = versuchsanzahl - 1
    if versuchsanzahl == 0:
        print("Du hast keine Versuche mehr übrig.")
    
if versuch == zahl:
    print("Du hast meine Zahl erraten!")