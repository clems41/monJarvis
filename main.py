print("Que voulez-vous faire ?")
fin = False
while not fin :
    choix = input("\n1/ LED 2/ Bras 0/ Quitter\n")
    if choix == 1 :
        execfile('led.py')
    elif choix == 2 :
        execfile('servo.py')
    elif choix == 0 :
        fin = True
    else :
        print("Ce choix n'est pas disponible !")
