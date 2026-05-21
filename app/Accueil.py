import pygame
from app.utils import getFont, get_dynamic_font_size
class Accueil:

    def __init__(self,x,y,width,height,cote,colorBorder,colorGame,colorFond):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.cote = cote
        border = pygame.Rect(self.x, self.y, self.width - self.cote * 2, self.height - self.cote * 2)
        font_size = get_dynamic_font_size('Snake Bidy', border.width,0.5)
        self.font = getFont(font_size)
        self.text = self.font.render('Snake Bidy', True, colorGame, colorFond)
        self.textRect = self.text.get_rect()
        self.textRect.center = (border.width / 2 + self.x, self.y + border.height / 3)
        self.border = border
        self.colorBorder = colorBorder
        taille_bouton = get_dynamic_font_size(' play ', border.width, max_allowed_pct=0.20)
        self.fontButton = getFont(taille_bouton)
        self.textButton = self.fontButton.render(' play ', True, colorFond, colorGame)
        self.textRectButton = self.textButton.get_rect()
        self.textRectButton.center = (border.width / 2 + self.x, self.y + border.height / 2 + self.cote*4)

    def dessinAcceuil(self,screen):
        screen.blit(self.textButton, self.textRectButton)
        screen.blit(self.text, self.textRect)
        pygame.draw.rect(screen, self.colorBorder, self.border, self.cote)