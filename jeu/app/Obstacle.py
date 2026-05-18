import pygame
import random
class Obstacle:

    def __init__(self,cote,x,y,width,height):
        self.obs = self.constructionSisiny(cote,x,y,width,height)
        self.taille = [1,2,3,4]
        self.width = width
        self.height = height
        self.cote = cote
        self.x1 = x
        self.y1 = y
        nbre = 20
        i = 0
        while i < nbre:
            while 0 < 9:
                if self.definitionObstacle() == False:
                    break
            i = i + 1

    def restartObstacle(self):
        self.obs.clear()
        self.obs.append(pygame.Rect(self.x1, self.y1, self.width - self.cote * 2, self.cote))
        self.obs.append(pygame.Rect(self.x1, self.y1 + self.height - self.cote * 3, self.width - self.cote, self.cote))
        self.obs.append(pygame.Rect(self.x1, self.y1, self.cote, self.height - self.cote * 2))
        self.obs.append(pygame.Rect(self.x1 + self.width - self.cote * 2, self.y1, self.cote, self.height - self.cote - self.cote))
        nbre = 20
        i = 0
        while i < nbre:
            while 0 < 9:
                if self.definitionObstacle() == False:
                    break
            i = i + 1

    def constructionSisiny(self,cote,x,y,width,height):
        i = 0
        tabSisiny = []
        tabSisiny.append(pygame.Rect(x,y,width - cote*2,cote))
        tabSisiny.append(pygame.Rect(x, y  + height - cote*3 , width -cote, cote))
        tabSisiny.append(pygame.Rect(x, y, cote, height-cote*2))
        tabSisiny.append(pygame.Rect(x + width - cote*2, y, cote,height-cote - cote))
        return tabSisiny

    def definitionObstacle(self):
        x = random.randint(1, (self.width - self.cote * 4) / self.cote)
        y = random.randint(1, (self.height - self.cote * 4) / self.cote)
        x = x * self.cote + self.x1
        y = y * self.cote + self.y1
        rect = pygame.Rect(x,y,self.taille[random.randint(0,len(self.taille) -1)] * self.cote,self.taille[random.randint(0,len(self.taille)-1)] * self.cote)
        i = 0
        b = False
        h = 0
        while i < len(self.obs):
           # if i < 4:
            sisiny = pygame.Rect(self.obs[i].x - self.cote,self.obs[i].y - self.cote,self.obs[i].width + self.cote*2,self.obs[i].height + self.cote*2)
            if self.intersection(sisiny,rect) == True:
                b = True
                break
            i = i + 1
        if b == False:
            self.obs.append(rect)
        return b

    def dessinObstacle(self,screen,color):
        i = 0
        while i < len(self.obs):
            pygame.draw.rect(screen, color, self.obs[i])
            i = i + 1

    def intersection(self,rect1,rect2):
        a = False
        maxgauche = max(rect1.x, rect2.x)
        mindroit = min(rect1.x + rect1.width, rect2.x + rect2.width)
        maxbas = max(rect1.y, rect2.y)
        minhaut = min(rect1.y + rect1.height, rect2.y + rect2.height)

        if maxgauche < mindroit and maxbas < minhaut:
            a = True
        return a