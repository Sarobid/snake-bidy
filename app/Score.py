import pygame
class Score:

    def __init__(self,x,y,width,height,fontColor,textColor):
        self.score = 0
        self.x = x
        self.y = y
        self.fontColor = fontColor
        self.textColor = textColor
        self.width = width
        self.height = height

    def dessinScore(self,screen,score):
        self.score = score
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.text = self.font.render('SCORE : ' + str(self.score), True, self.textColor, self.fontColor)
        self.textRect = self.text.get_rect()
        self.textRect.center = (self.width / 2 + self.x, self.y)
        screen.blit(self.text, self.textRect)
