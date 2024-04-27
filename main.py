# Importation des modules
from common.NimGame import initValues
from utils.ScreenUtils import Screen

# Initialisation des valeurs
initValues()

# Création de l'écran de l'application
screen = Screen("Jeu d'Allumette")

# Définition de la fonction de démarrage du jeu
def startGame():
    """
    Démarre le jeu
    """
    # Importation de la fonction de manière locale pour éviter les dépendances circulaires
    from ui.MainScreen import showMainScreen

    # Affichage de l'écran principal
    showMainScreen(screen)
    
# Démarrage du jeu
startGame()