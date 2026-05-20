import pygame
from app.utils import getFont

class Score:

    def __init__(self,x,y,width,height,fontColor,textColor):
        self.score = 0
        self.x = x
        self.y = y
        self.fontColor = fontColor
        self.textColor = textColor
        self.width = width
        self.height = height
        self.meilleur = 0

    def dessinScore(self,screen,score):
        self.score = score
        if self.score >= self.meilleur:
            self.meilleur = self.score
        self.font = getFont(20)
        self.text = self.font.render('SCORE : ' + str(self.score), True, self.textColor, self.fontColor)
        self.textRect = self.text.get_rect()
        self.textRect.center = (self.width / 2 + self.x, self.y)
        screen.blit(self.text, self.textRect)
        self.fontH = getFont(20)
        self.textH = self.fontH.render('BEST SCORE : ' + str(self.meilleur), True, self.textColor, self.fontColor)
        self.textRectH = self.textH.get_rect()
        self.textRectH.center = (100 + self.x, self.y)
        RED = (255, 0, 0)
        GREEN = (0, 255, 0)
        self.fontS = getFont(20)
        self.textS = self.fontS.render('Snake Bidy', True, GREEN, RED)
        self.textRectS = self.textS.get_rect()
        self.textRectS.center = (self.width  - self.x - 20, self.y)
        screen.blit(self.textS, self.textRectS)
        screen.blit(self.textH, self.textRectH)
