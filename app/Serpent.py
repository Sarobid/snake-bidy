import pygame
class Serpent:

    def __init__(self,cote,x,y):
        self.x = x
        self.y = y
        self.mooveX = 0
        self.mooveY = cote
        self.serp = []
        self.tailleI = 4
        self.cote = cote
        self.initialisationSepent()
        self.maty = 0

    def midona(self,obs):
        i = 1
        while i < len(self.serp):
            if self.serp[0].contains(self.serp[i]) == True:
                self.maty = 1
                #sprint("midona")
            i = i + 1
        self.midonaObstacle(obs)

    def midonaObstacle(self,obs):
        i = 0
        while i < len(obs):
            if obs[i].contains(self.serp[0]) == True:
                self.maty = 1
                #print("midona")
            i = i + 1

    def mooveAutomatique(self):
        if self.maty == 0:
            self.moove(self.x, self.y)
            a = 0
            if self.x < self.serp[0].x:
                self.mooveX = + self.cote
                self.mooveY = 0
            elif self.x > self.serp[0].x:
                self.mooveX = - self.cote
                self.mooveY = 0
            elif self.y > self.serp[0].y:
                self.mooveX = 0
                self.mooveY = - self.cote
            elif self.y < self.serp[0].y:
                self.mooveX = 0
                self.mooveY = + self.cote
            self.serp[0].x = self.serp[0].x + self.mooveX
            self.serp[0].y = self.serp[0].y + self.mooveY
            self.x = self.serp[0].x
            self.y = self.serp[0].y


    def initialisationSepent(self):
        i = 0
        x1 = self.x
        y1 = self.y
        while i < self.tailleI:
            self.serp.append(pygame.Rect(x1,y1,self.cote,self.cote))
            x1 = x1 + self.cote
            i = i + 1

    def deplacement(self,indice,x,y):
       if indice < len(self.serp):
           self.deplacement(indice + 1, self.serp[indice].x, self.serp[indice].y)
           self.serp[indice].x = x
           self.serp[indice].y = y

    def moove(self,x,y):
        self.deplacement(1,x,y)

    def dessinSerpent(self,screen,tete,color):
        i = 1
        pygame.draw.rect(screen, tete, self.serp[0])
        while i < len(self.serp):
            pygame.draw.rect(screen,color,self.serp[i])
            i = i + 1