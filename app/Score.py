import pygame
from app.utils import getFont, get_dynamic_font_size

class Score:

    def __init__(self,x,y,cote,width,height,fontColor,textColor):
        self.score = 0
        self.x = x
        self.y = y - cote
        self.fontColor = fontColor
        self.textColor = textColor
        self.width = width
        self.height = height
        self.meilleur = 90
        self.padding = 10
        self.font_size = get_dynamic_font_size('BEST SCORE: 100', self.width, max_allowed_pct=0.15)

    def dessinScore(self,screen,score):
        self.score = score
        if self.score >= self.meilleur:
            self.meilleur = self.score
        self._dessinBestScore(screen)
        self._dessinCurrentScore(screen)
        self._dessin_title_snake_bidy(screen)

    def  _dessinBestScore(self,screen):
        best_score_text = 'BEST SCORE: ' + str(self.meilleur)
        self.fontH = getFont(self.font_size)
        self.textH = self.fontH.render(best_score_text, True, self.textColor, self.fontColor)
        self.textRectH = self.textH.get_rect()
        self.textRectH.left = self.x + self.padding
        self.textRectH.centery = self.y
        screen.blit(self.textH, self.textRectH)

    def _dessinCurrentScore(self,screen):
        current_score_text = 'SCORE: ' + str(self.score)
        self.fontC = getFont(self.font_size)
        self.textC = self.fontC.render(current_score_text, True, self.textColor, self.fontColor)
        self.textRectC = self.textC.get_rect()
        self.textRectC.right = self.x + self.width - self.padding - (self.textRectC.width//2)
        self.textRectC.centery = self.y
        screen.blit(self.textC, self.textRectC)

    def _dessin_title_snake_bidy(self,screen):
        RED = (255, 0, 0)
        GREEN = (0, 255, 0)
        title_text = 'Snake Bidy'
        self.font_title = getFont(get_dynamic_font_size(title_text, self.width, max_allowed_pct=0.25))
        self.text_title = self.font_title.render(title_text, True, GREEN, RED)
        self.textRect_title = self.text_title.get_rect()
        self.textRect_title.centerx = self.x + (self.width // 2)
        self.textRect_title.y = self.y - self.textRect_title.height // 2 - self.padding
        screen.blit(self.text_title, self.textRect_title)
