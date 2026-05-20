import pygame
import os

def getFont(size: int) -> pygame.font.Font:
    size = size - 10
    font_path = "./data/font/press_start_2p/PressStart2P-Regular.ttf"
    if os.path.exists(font_path):
        return pygame.font.Font(font_path, size)
    else:
        print(f"⚠️ Alerte Designer : Fichier {font_path} introuvable. Utilisation de la police par défaut.")
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
    """
    Calcule les dimensions maximales de la zone de jeu (width, height)
    en appliquant des pourcentages de marge personnalisés pour chaque côté,
    tout en garantissant un alignement parfait sur la grille (cote).
    """
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