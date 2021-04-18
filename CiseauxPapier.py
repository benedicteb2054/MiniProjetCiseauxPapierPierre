import random
choix=['C','P','Pi']
score_cpu=0
score_joueur=0

while True:
    cpu = random.choice(choix)
    joueur = str(input('C: Ciseaux, P:Papier ou Pi: Pierre? pour terminer taper Fin')).capitalize()
    if joueur==cpu:
        print("égalité!")
    elif joueur=='Pi':
        if cpu=='p':
            print('Vous perdez, le papier couvre la pierre')
            score_cpu+=1
        elif cpu=='C':
            print('vous gagnez, la pierre casse les ciseaux')
            score_joueur+=1

    elif joueur=='P':
        if cpu=='Pi':
            print('Vous gagnez, le papier couvre la pierre')
            score_joueur+=1
        elif cpu=='C':
            print('vous perdez, les ciseaux coupent le papier')
            score_cpu += 1

    elif joueur=='C':
        if cpu=='Pi':
            print('Vous perdez, la pierre casse les ciseaux')
        elif cpu=='P':
            print('vous gagnez, les ciseaux coupent le papier')
            score_joueur += 1

    elif joueur=='Fin':
        print("resultat:")
        print(f"CPU: {score_cpu}")
        print(f"joueur: {score_joueur}")
        break
    else:
        print("je n'ai pas compris, verifier l'orthographe")