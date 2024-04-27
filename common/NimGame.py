# Définition des variables globales
matches = 16
difficulty = 1
maxNumberOfMatchesTakeable = 3
mode = 1
firstPlayerName = "Joueur1"
secondPlayerName = "Joueur2"

# Définition des fonctions
def initValues():
    """
    Initialise les variables globales
    """
    global matches, difficulty, maxNumberOfMatchesTakeable, mode, firstPlayerName, secondPlayerName
    matches = 21
    difficulty = 1
    maxNumberOfMatchesTakeable = 3
    mode = 1
    firstPlayerName = "Joueur1"
    secondPlayerName = "Joueur2"

def getFirstPlayerName():
    """
    Retourne le nom du premier joueur local
    """
    global firstPlayerName
    return firstPlayerName

def getSecondPlayerName():
    """
    Retourne le nom du second joueur local
    """
    global secondPlayerName
    return secondPlayerName

def setFirstPlayerName(value):
    """
    Définit le nom du premier joueur local

    Paramètres:
    * value: le nom du premier joueur local
    """
    global firstPlayerName
    firstPlayerName = value

def setMode(value):
    """
    Définit le mode de jeu

    Paramètres:
    * value: la valeur du mode de jeu (1 = Solo | 2 = Local)
    """
    global mode
    mode = value

def setSecondPlayerName(value):
    """
    Définit le nom du second joueur local

    Paramètres:
    * value: le nom du second joueur local
    """
    global secondPlayerName
    secondPlayerName = value

def setMatches(value):
    """
    Définit le nombre d'allumettes

    Paramètres:
    * value: le nombre d'allumettes
    """
    global matches
    matches = value

def setDifficulty(value):
    """
    Définit la difficulté

    Paramètres:
    * value: la difficulté
    """
    global difficulty
    difficulty = value

def setMaxNumberOfMatchesTakeable(value):
    """
    Définit le nombre maximum d'allumettes pouvant être prises

    Paramètres:
    * value: le nombre maximum d'allumettes pouvant être prises
    """
    global maxNumberOfMatchesTakeable
    maxNumberOfMatchesTakeable = value

def getMode():
    """
    Retourne le mode de jeu
    """
    global mode
    return mode

def getMatches():
    """
    Retourne le nombre d'allumettes
    """
    global matches
    return matches

def getDifficulty():
    """
    Retourne la difficulté
    """
    global difficulty
    return difficulty

def getMaxNumberOfMatchesTakeable():
    """
    Retourne le nombre maximum d'allumettes pouvant être prises
    """
    global maxNumberOfMatchesTakeable
    return maxNumberOfMatchesTakeable