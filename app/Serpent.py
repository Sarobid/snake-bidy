import pygame
class Serpent:

    def __init__(self,cote,x,y):
        self.x = x
        self.y = y
        self.x0 = x
        self.y0 = y
        self.mooveX = 0
        self.mooveY = cote
        self.serp = []
        self.tailleI = 4
        self.cote = cote
        self.initialisationSepent()
        self.maty = 0
        self.demarer = False

    def restartSerp(self):
        i = 0
        self.serp.clear()
        self.maty = 0
        self.demarer = False
        x1 = self.x0
        y1 = self.y0
        self.x = x1
        self.y = y1
        while i < self.tailleI:
            self.serp.append(pygame.Rect(x1, y1, self.cote, self.cote))
            x1 = x1 + self.cote
            i = i + 1
    def midona(self,obs,sonsMaty):
        i = 1
        while i < len(self.serp):
            if self.serp[0].contains(self.serp[i]) == True:
                self.maty = 1
                sonsMaty.play()
                #sprint("midona")
            i = i + 1
        self.midonaObstacle(obs,sonsMaty)

    def midonaObstacle(self,obs,sonsMaty):
        i = 0
        while i < len(obs):
            if obs[i].contains(self.serp[0]) == True:
                self.maty = 1
                #print("midona")
                sonsMaty.play()
            i = i + 1

    def mooveAutomatique(self):

        if self.maty == 0 and self.demarer == True:
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

    def moveUp(self):
        self.demarer = True
        self.mooveY = -self.cote
        self.mooveX = 0
    
    def moveDown(self):
        self.demarer = True
        self.mooveY = +self.cote
        self.mooveX = 0
    
    def moveLeft(self):
        self.demarer = True
        self.mooveX = -self.cote
        self.mooveY = 0

    def moveRight(self):
        self.demarer = True
        self.mooveX = +self.cote
        self.mooveY = 0

    def playOrPause(self):
        if self.demarer == True:
            self.demarer = False
        elif self.demarer == False:
            self.demarer = True

    def dessinSerpent(self,screen,tete,color):
        i = 1
        pygame.draw.rect(screen, tete, self.serp[0])
        while i < len(self.serp):
            pygame.draw.rect(screen,color,self.serp[i])
            i = i + 1