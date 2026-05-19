import pygame
class Accueil:

    def __init__(self,x,y,width,height,cote,colorBorder,colorGame,colorFond):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.cote = cote
        border = pygame.Rect(self.x, self.y, self.width - self.cote * 2, self.height - self.cote * 2)
        self.font = pygame.font.Font(None, 70)
        self.text = self.font.render('Snake Bidy', True, colorGame, colorFond)
        self.textRect = self.text.get_rect()
        self.textRect.center = (border.width / 2 + self.x, self.y + border.height / 3)
        self.border = border
        self.colorBorder = colorBorder
        self.fontButton = pygame.font.Font(None, 30)
        self.textButton = self.fontButton.render(' play ', True, colorFond, colorGame)
        self.textRectButton = self.textButton.get_rect()
        self.textRectButton.center = (border.width / 2 + self.x, self.y + border.height / 2 + self.cote*4)

    def dessinAcceuil(self,screen):
        screen.blit(self.textButton, self.textRectButton)
        screen.blit(self.text, self.textRect)
        pygame.draw.rect(screen, self.colorBorder, self.border, self.cote)