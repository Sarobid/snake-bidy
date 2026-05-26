import pygame
import os

def positionnerRectZCentreVerticalementAGauche(rectExt: pygame.Rect, rectInt: pygame.Rect, rectZ: pygame.Rect) -> pygame.Rect:
    rectZ.x = rectExt.left
    rectZ.y = rectInt.top + (rectInt.height - rectZ.height) // 2    
    return rectZ

def positionnerRectZCentreVerticalementADroite(rectExt: pygame.Rect, rectInt: pygame.Rect, rectZ: pygame.Rect) -> pygame.Rect:
    rectZ.x = rectExt.right - rectZ.width
    rectZ.y = rectInt.top + (rectInt.height - rectZ.height) // 2
    
    return rectZ
def diviser_rect(rect: pygame.Rect, nbre_parts: int, orientation: str = "vertical") -> list[pygame.Rect]:
    liste_rectangles = []
    
    if nbre_parts <= 0:
        return liste_rectangles

    if orientation == "vertical":
        # Découpage en colonnes : la largeur change, la hauteur reste identique
        largeur_part = rect.width // nbre_parts
        hauteur_part = rect.height
        
        for i in range(nbre_parts):
            nouvel_x = rect.x + (i * largeur_part)
            nouvel_y = rect.y
            liste_rectangles.append(pygame.Rect(nouvel_x, nouvel_y, largeur_part, hauteur_part))
            
    elif orientation == "horizontal":
        # Découpage en lignes : la hauteur change, la largeur reste identique
        largeur_part = rect.width
        hauteur_part = rect.height // nbre_parts
        
        for i in range(nbre_parts):
            nouvel_x = rect.x
            nouvel_y = rect.y + (i * hauteur_part)
            liste_rectangles.append(pygame.Rect(nouvel_x, nouvel_y, largeur_part, hauteur_part))
            
    return liste_rectangles

def appliquer_padding_rect(rect: pygame.Rect, padding: int) -> pygame.Rect:
    rect.inflate_ip(-2 * padding, -2 * padding)
    return rect

def getResteRectBasInRectExtAndRectInt(rectExt: pygame.Rect, rectInt: pygame.Rect) -> pygame.Rect:
    """
    Calcule et retourne la zone libre (x, y, width, height) située en bas,
    entre le rectangle intérieur (le Stade) et le rectangle extérieur (l'Écran).
    Idéal pour positionner le VirtualGamepad sur mobile.
    """
    x = rectExt.left
    y = rectInt.bottom
    width = rectExt.width
    height = rectExt.bottom - rectInt.bottom
    if height < 0:
        height = 0
    return pygame.Rect(x, y, width, height)

def isIntersection(rect1,rect2):
    a = False
    maxgauche = max(rect1.x, rect2.x)
    mindroit = min(rect1.x + rect1.width, rect2.x + rect2.width)
    maxbas = max(rect1.y, rect2.y)
    minhaut = min(rect1.y + rect1.height, rect2.y + rect2.height)

    if maxgauche < mindroit and maxbas < minhaut:
        a = True
    return a

def getFont(size: int) -> pygame.font.Font:
    # size = size - 10
    font_path = "./data/font/press_start_2p/PressStart2P-Regular.ttf"
    if os.path.exists(font_path):
        return pygame.font.Font(font_path, size)
    else:
        return pygame.font.Font(None, size)
    

def calculer_dimensions_jeu(
    widthScreen: int, 
    heightScreen: int, 
    cote: int, 
    pct_gauche: float = 0.05,  # 5% de marge à gauche par défaut
    pct_droite: float = 0.05,  # 5% de marge à droite par défaut
    pct_haut: float = 0.10,    # 10% de marge en haut par défaut (pour le score)
    pct_bas: float = 0.05      # 5% de marge en bas par défaut
) -> tuple[int, int]:
    # 1. On calcule la taille des marges en pixels en fonction de l'écran
    marge_gauche = widthScreen * pct_gauche
    marge_droite = widthScreen * pct_droite
    marge_haut = heightScreen * pct_haut
    marge_bas = heightScreen * pct_bas
    
    # 2. On déduit l'espace maximal restant pour la zone de jeu
    espace_dispo_w = widthScreen - (marge_gauche + marge_droite)
    espace_dispo_h = heightScreen - (marge_haut + marge_bas)
    
    # 3. DIVISION ENTIÈRE (//) : On trouve le nombre maximal de cases
    nb_cases_width = int(espace_dispo_w // cote)
    nb_cases_height = int(espace_dispo_h // cote)
    
    # Sécurité minimale pour éviter une zone de jeu invisible
    if nb_cases_width < 10: nb_cases_width = 10
    if nb_cases_height < 10: nb_cases_height = 10
    
    # 4. Conversion finale en pixels exacts (multiples de 'cote')
    width_jeu = nb_cases_width * cote
    height_jeu = nb_cases_height * cote
    
    return width_jeu, height_jeu

def get_dynamic_font_size(text: str, target_width: int, max_allowed_pct: float = 0.50) -> int:
    # Une règle empirique propre : à la taille 10, chaque caractère d'une police 
    # standard occupe environ 6 à 7 pixels de large. 
    # Pour 'Snake Bidy' (10 caractères), on estime la taille idéale :
    nb_caracteres = len(text)
    
    # Largeur que le texte DOIT occuper au maximum en pixels
    largeur_cible_pixels = target_width * max_allowed_pct
    
    # Formule prédictive pour estimer la taille en points (fontSize)
    # On divise par le nombre de caractères et un facteur de proportionnalité (0.6)
    font_size = int(largeur_cible_pixels / (nb_caracteres * 0.6))
    
    # Sécurités : On évite une police géante ou invisible
    if font_size > 100: font_size = 100
    # if font_size < 20: font_size = 20
        
    return font_size