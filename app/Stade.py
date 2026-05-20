import pygame
class Stade:
    def __init__(self,cote,width,height,widthScreen,heightScreen):
        self.cote = cote
        self.width = width
        self.height = height
        self.widthScreen = widthScreen
        self.heightScreen = heightScreen
        self.constructionStade()
        
    def get_xStart(self):
        return (self.widthScreen - self.width) // 2

    def get_yStart(self):
        return (self.heightScreen - self.height) // 2
    
    def constructionStade(self):
        i = 0
        self.tab = []
        x0 = self.get_xStart()
        y0 = self.get_yStart()
        x1 = self.get_xStart()
        y1 = self.get_yStart()
        widhMax = self.width + x0 - self.cote * 2
        heightMax = self.height + y0 - self.cote * 2
        #Verticale
        while x1 <= widhMax:
            self.tab.append(pygame.Rect(x1,y1,x1,heightMax))
            x1 = x1 + self.cote
        #Horizontale
        x1 = self.get_xStart()
        y1 = self.get_yStart()
        while y1 <= heightMax:
            self.tab.append(pygame.Rect(x1,y1,widhMax,y1))
            y1 = y1 + self.cote

    def dessinStade(self,screen,color):
        i = 0
        while i < len(self.tab):
            pygame.draw.aaline(screen,color , (self.tab[i].x, self.tab[i].y), (self.tab[i].width, self.tab[i].height))
            i = i + 1