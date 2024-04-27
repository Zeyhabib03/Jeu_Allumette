from utils.ScreenUtils import *
import random

def showMatchScreen(screen):
    """
    Affiche l'écran de jeu
    """
    # Importation de la fonction de manière locale pour éviter les dépendances circulaires
    from common.NimGame import getMaxNumberOfMatchesTakeable, getMatches, setMatches, getDifficulty, getMode, getFirstPlayerName, getSecondPlayerName, initValues
    from ui.MainScreen import showMainScreen

    # Nettoyer l'écran
    screen.clear_elements()

    # Ajout du fond de fenêtre
    background = Picture(0, 0, "./ressources/images/background.png")
    background.resize(1280, 720)

    # Création des éléments
    if(getMode() == 1):
        current_turn = 1
        sideArea = Area(360, 25, 600, 100)
        title = Text(380, 25, "A Votre Tour !", 70)
    elif(getMode() == 2):
        current_turn = random.randint(0,1)
        sideArea = Area(150, 25, 1000, 100)
        if(current_turn == 0):
            title = Text(190, 35, ("Au tour de " + getSecondPlayerName()), 50)
        else:
            title = Text(190, 35, ("Au tour de " + getFirstPlayerName()), 50)
    mainArea = Area(40, 175, 1200, 500)

    matchesText = Text(0, 350, "", 90)

    def updateMatchesLocation():
        """
        Fonction pour mettre à jour les allumettes
        """
        matchesText.text = ""
        for _ in range(getMatches()):
            matchesText.text += "|"
        matchesTextWidth = 20 * getMatches()
        matchesTextX = (1280 - matchesTextWidth) / 2
        matchesText.x = matchesTextX
    
    updateMatchesLocation()

    # Définition des événements des boutons
    def homeButtonEvent():
        """
        Retourne à l'écran d'accueil
        """
        initValues()
        showMainScreen(screen)

    def backButtonEvent():
        """
        Retourne à l'écran d'accueil
        """
        initValues()
        showMainScreen(screen)

    def validateButtonEvent():
        """
        Valide le nombre d'allumettes à prendre
        """
        nonlocal current_turn
        if(getMode() == 1): # Mode solo
            if title.text == "A Votre Tour !":
                playerMatchesTaken = int(matchesValue.text)
                setMatches(getMatches() - playerMatchesTaken)
                matchesNumber.text = "Allumettes restantes : " + str(getMatches())
                matchesValue.text = "1"
                checkGameResult()
                current_turn = 1 # Changer le tour après que le joueur a joué
                botTurn() #Tour de l'IA

        elif(getMode() == 2): # Mode local
            playerMatchesTaken = int(matchesValue.text)
            setMatches(getMatches() - playerMatchesTaken)
            matchesNumber.text = "Allumettes restantes : " + str(getMatches())
            matchesValue.text = "1"
            if(current_turn == 1):
                title.text = ("Au tour de " + getSecondPlayerName())
                checkGameResult() # Vérifier si la partie est terminée
                current_turn = 0
            else:
                title.text = ("Au tour de " + getFirstPlayerName())
                checkGameResult() # Vérifier si la partie est terminée
                current_turn = 1
        updateMatchesLocation()
            
    def removeMaxTakenMatchesButtonEvent():
        """
        Diminue le nombre d'allumettes prises
        """
        currentValue = int(matchesValue.text)
        if currentValue > 1:
            matchesValue.setText(str(currentValue - 1))

    def addMaxTakenMatchesButtonEvent():
        """
        Augmente le nombre d'allumettes prises
        """
        currentValue = int(matchesValue.text)
        if currentValue < getMaxNumberOfMatchesTakeable():
            if currentValue < getMatches():
                matchesValue.setText(str(currentValue + 1))

    # Création des boutons
    increaseButton = Button(740, 550, "+", addMaxTakenMatchesButtonEvent, 95, 95)
    matchesValue = Button(600, 550, "1", lambda: None, 95, 95)
    matchesNumber = Button(600, 250, ("Allumettes restantes : " + str(getMatches())), lambda: None, 95, 95, "#DED0B6", "#DED0B6")
    decreaseButton = Button(450, 550, "-", removeMaxTakenMatchesButtonEvent, 95, 95)
    validateButton = Button(950, 550, "Valider", validateButtonEvent, 250, 85)
    returnButton = Button(75, 550, "Retour", backButtonEvent, 250, 85)

    # Ajout des éléments à l'écran
    screen.add_element(background)
    screen.add_element(mainArea)
    screen.add_element(sideArea)
    screen.add_element(title)
    screen.add_element(returnButton)
    screen.add_element(validateButton)
    screen.add_element(increaseButton)
    screen.add_element(matchesValue)
    screen.add_element(decreaseButton)
    screen.add_element(matchesNumber)
    screen.add_element(matchesText)

    # Définition des fonctions relatives au jeu
    def checkGameResult():
        """
        Vérifie si la partie est terminée
        """
        if getMatches() == 0:
            accueil = Button(475, 550, "Réjouer", homeButtonEvent)
            menuArea = Area(40, 525, 1200, 150)
            title.setText(" ")
            screen.add_element(menuArea)
            screen.add_element(accueil)
            if getMode() == 1:
                if current_turn == 1:
                    winText = Text(515, 35, "Gagné ! :D", 50)
                    screen.add_element(winText)
                else:
                    looseText = Text(515, 35, "Perdu ! :(", 50)
                    screen.add_element(looseText)
            elif getMode() == 2:
                if current_turn == 0:
                    winText = Text(190, 35, f"Victoire de {getFirstPlayerName()}", 50)
                else:
                    winText = Text(190, 35, f"Victoire de {getSecondPlayerName()}", 50)
                screen.add_element(winText)

    def calculateNimSum():
        """
        Calculer le nim-sum
        """
        matches = getMatches()
        max_takeable = getMaxNumberOfMatchesTakeable()

        if matches % (max_takeable + 1) == 0:
            return 0
        else:
            return matches % (max_takeable + 1)

    def botTurn():
        """
        Tour de l'IA
        """
        nonlocal current_turn

        if getMode() == 1:
            if getDifficulty() == 1:  # Mode facile - Forte probabilité de gagner
                if getMatches() > 0:
                    matchesTaken = min(random.randint(1, getMaxNumberOfMatchesTakeable()), getMatches())
                    setMatches(getMatches() - matchesTaken)
                    matchesNumber.text = "Allumettes restantes : " + str(getMatches())
                    checkGameResult()
                    current_turn = 0  # Changer le tour après que l'IA a joué

            elif getDifficulty() == 2:  # Mode moyen - Probabilité moyenne de gagner
                if getMatches() > 0:
                    found_valid_move = False # Variable pour vérifier si un coup valide a été trouvé pour laisser 1 allumette à l'adversaire
                    for i in range(1, getMaxNumberOfMatchesTakeable() + 1):
                        if (getMatches() - i == 1):
                            matchesTaken = i
                            found_valid_move = True
                            break

                    if not found_valid_move: # Impossible de faire en sorte de laisser 1 allumette à l'adversaire
                        # Utilisation d'une approche probabiliste
                        if random.random() < 0.7:  # 70% de chances de jouer de manière aléatoire
                            matchesTaken = min(random.randint(1, getMatches()), getMaxNumberOfMatchesTakeable())
                        else:
                            # Calculer le nim-sum
                            nim_sum = calculateNimSum()
                            # Si le nim-sum est non nul, jouer de manière intelligente
                            if nim_sum != 0:
                                matchesTaken = getMatches() % (getMaxNumberOfMatchesTakeable() + 1)
                            else:
                                # Sinon, jouer de manière aléatoire
                                matchesTaken = min(random.randint(1, getMatches()), getMaxNumberOfMatchesTakeable())

                    setMatches(getMatches() - matchesTaken)
                    matchesNumber.text = "Allumettes restantes : " + str(getMatches())
                    checkGameResult()
                    current_turn = 0  # Changer le tour après que l'IA a joué

            else:  # Mode difficile - Probabilité faible de gagner
                if getMatches() > 0:
                    found_valid_move = False # Variable pour vérifier si un coup valide a été trouvé pour laisser 1 allumette à l'adversaire
                    for i in range(1, getMaxNumberOfMatchesTakeable() + 1):
                        if (getMatches() - i == 1):
                            matchesTaken = i
                            found_valid_move = True
                            break
                    if not found_valid_move: # Impossible de faire en sorte de laisser 1 allumette à l'adversaire
                        if getMatches() == 1:
                            matchesTaken = 1
                        else:
                            matchesTaken = getMatches() % (getMaxNumberOfMatchesTakeable() + 1)
                            # Si nim-sum est 0, jouer de manière aléatoire
                            if calculateNimSum() == 0:
                                matchesTaken = random.randint(1, min(getMatches(), getMaxNumberOfMatchesTakeable()))
                    setMatches(getMatches() - matchesTaken)
                    matchesNumber.text = "Allumettes restantes : " + str(getMatches())
                    checkGameResult()
                    current_turn = 0  # Changer le tour après que l'IA a joué

            updateMatchesLocation()

    # Lancer la fenêtre
    screen.run()