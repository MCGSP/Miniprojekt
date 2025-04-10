import random
spieler = random.randint(1,6)
computer = random.randint(1,6)
spielerGewinnt = 0
computerGewinnt = 0
runde = 0
while runde < 5:
    if spieler > computer:
        runde = runde + 1
        spielerGewinnt = spielerGewinnt + 1
        print("Du hast eine " + str(spieler) + " gewürfelt, und ich habe eine " + str(computer) + " gewürfelt. Ein Punkt für dich!")
        print("Es steht " + str(spielerGewinnt) + " zu " + str(computerGewinnt) + ".")
    elif spieler < computer:
        runde = runde + 1
        computerGewinnt = computerGewinnt + 1
        print("Du hast eine " + str(spieler) + " gewürfelt, und ich habe eine " + str(computer) + " gewürfelt. Ein Punkt für mich!")
        print("Es steht " + str(spielerGewinnt) + " zu " + str(computerGewinnt) + ".")
    elif spieler == computer:
        print("Du hast eine " + str(spieler) + " gewürfelt, und ich habe eine " + str(computer) + " gewürfelt. Das ist ein Unentschieden.")
        
if spielerGewinnt > computerGewinnt:
    print("Der Endstand ist " + str(spielerGewinnt) + " zu " + str(computergewinnt) +  ". Du hast gewonnen!")