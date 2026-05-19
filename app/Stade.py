import pygame
class Stade:
    def __init__(self,cote,width,height):
        self.cote = cote
        self.width = width
        self.height = height
        self.constructionStade()
        
    def get_xStart(self):
        return self.cote * 2

    def get_yStart(self):
        return self.cote * 2
    
    def constructionStade(self):
        i = 0
        self.tab = []
        x1 = self.get_xStart()
        y1 = self.get_yStart()
        #Verticale
        while x1 <= self.width:
            self.tab.append(pygame.Rect(x1,y1,x1,self.height))
            x1 = x1 + self.cote
        #Horizontale
        x1 = self.get_xStart()
        y1 = self.get_yStart()
        while y1 <= self.height:
            self.tab.append(pygame.Rect(x1,y1,self.width,y1))
            y1 = y1 + self.cote

    def dessinStade(self,screen,color):
        i = 0
        while i < len(self.tab):
            pygame.draw.aaline(screen,color , (self.tab[i].x, self.tab[i].y), (self.tab[i].width, self.tab[i].height))
            i = i + 1