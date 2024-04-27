from utils.ScreenUtils import *
import sys

def showMainScreen(screen):
    """
    Affiche l'écran principal
    """
    # Importation de la fonction de manière locale pour éviter les dépendances circulaires
    from ui.SoloScreen import showSoloScreen
    from ui.LocalScreen import showLocalScreen
    from common.NimGame import setMode

    # Nettoyer l'écran
    screen.clear_elements()
    
    # Ajout du fond de fenêtre
    background = Picture(0,0, "./ressources/images/background.png")
    background.resize(1280,720)

    # Création des éléments
 
    title = Text(390,85,"Allumette",70,)

    menuArea = Area(350,75,550,550)

    # Définition des événements des boutons
    def soloButtonEvent():
        """
        Affiche l'écran de jeu solo
        """
        setMode(1)
        showSoloScreen(screen)
        
    def localButtonEvent():
        """
        Affiche l'écran de jeu local
        """
        setMode(2)
        showLocalScreen(screen)

    def quitButtonEvent():
        """
        Affiche l'écran de jeu en ligne
        """
        sys.exit()

    # Création des boutons
    soloButton = Button(410,190,"Joueur vs PC",soloButtonEvent,425,105)
    localButton = Button(410,325,"Multijoueur",localButtonEvent,425,105)
    quitButton = Button(410,460,"Quitter",quitButtonEvent,425,105)

    # Ajout des éléments à l'écran
    screen.add_element(background)
    screen.add_element(menuArea)
    screen.add_element(soloButton)
    screen.add_element(localButton)
    screen.add_element(quitButton)
    screen.add_element(title)

    # Lancer la fenêtre
    screen.run()