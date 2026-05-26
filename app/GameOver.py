import pygame
from app.utils import getFont, get_dynamic_font_size
class GameOver:

    def __init__(self,x,y,width,height,cote,colorBorder,colorGame,colorFond):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.cote = cote
        self.colorBorder = colorBorder

        border = pygame.Rect(self.x, self.y, self.width, self.height)
        font_size = get_dynamic_font_size('Game Over', border.width, 0.5)
        self.font = getFont(font_size)
        self.text = self.font.render('Game Over', True, colorGame, colorFond)
        self.textRect = self.text.get_rect()
        self.textRect.center = (border.width / 2 + self.x, self.y + border.height / 3)
        RED = (255, 0, 0)

        taille_bouton = get_dynamic_font_size('restart', border.width, max_allowed_pct=0.20)
        self.fontButton = getFont(taille_bouton)
        self.textButton = self.fontButton.render('restart', True, colorGame, RED)
        self.textRectButton = self.textButton.get_rect()
        self.textRectButton.center = (border.width / 2 + self.x, self.y + border.height / 3 * 2)
        self.border = border

    def afficheGameOver(self,screen,score):

        screen.blit(self.textButton,self.textRectButton)
        screen.blit(self.text, self.textRect)
        pygame.draw.rect(screen, self.colorBorder, self.border,self.cote)



