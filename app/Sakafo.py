import pygame
import random
from app.Obstacle import Obstacle
class Sakafo:

    def __init__(self,obstacle,x,y,width,height,cote,color):
        self.pastec = pygame.Rect(x,y,cote,cote)
        self.color = color
        self.width = width
        self.height = height
        self.cote = cote
        self.obstacle = obstacle
        self.definitionEmplacement(x,y)
        self.x1 = x
        self.y1 = y
        self.score = 0

    def dessinSakafo(self,screen):
        pygame.draw.rect(screen, self.color, self.pastec)

    def definitionEmplacement(self,x1,y1):
        self.defEmp(x1,y1)

    def defEmp(self,x1,y1):
        x = random.randint(1, (self.width - self.cote * 4) / self.cote)
        y = random.randint(1, (self.height - self.cote * 4) / self.cote)
        self.pastec.x = x * self.cote + x1
        self.pastec.y = y * self.cote + y1
        a = False
        i = 0
        obs = self.obstacle.obs
        while i < len(obs):
            if self.obstacle.intersection(self.pastec,obs[i]) == True:
                a = True
                break
            i = i + 1
        if a == True:
            a = False
            self.defEmp(x1,y1)

    def voaHinana(self,serpent):
        serp = serpent.serp
        maxgauche = self.pastec.x
        if self.pastec.x < serp[0].x:
            maxgauche = serp[0].x
        mindroit = self.pastec.x + self.pastec.width
        if self.pastec.x + self.pastec.width > serp[0].x + serp[0].width:
            mindroit = serp[0].x + serp[0].width
        maxbas = self.pastec.y
        if self.pastec.y < serp[0].y:
            maxbas = serp[0].y
        minhaut = self.pastec.y + self.pastec.height
        if self.pastec.y + self.pastec.height > serp[0].y + serp[0].height:
            minhaut =  serp[0].y + serp[0].height
        if maxgauche < mindroit and maxbas < minhaut:
            x = serp[len(serp) -1].x + (-1)*serpent.mooveX
            y = serp[len(serp) - 1].y + (-1) * serpent.mooveY
            serp.append(pygame.Rect(x,y,serp[0].width,serp[0].width))
            self.definitionEmplacement(self.x1,self.y1)
            self.score = self.score + 1
