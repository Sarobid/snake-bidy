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