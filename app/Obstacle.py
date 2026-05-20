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
        self.nbreObstacle = self.calculer_nombre_obstacles()
        nbre = self.nbreObstacle
        i = 0
        while i < nbre:
            while 0 < 9:
                if self.definitionObstacle() == False:
                    break
            i = i + 1
    def set_best_score(self, best_score: int):
        self.nbreObstacle = self.calculer_nombre_obstacles(best_score)

    def restartObstacle(self):
        self.obs.clear()
        self.obs.append(pygame.Rect(self.x1, self.y1, self.width - self.cote * 2, self.cote))
        self.obs.append(pygame.Rect(self.x1, self.y1 + self.height - self.cote * 3, self.width - self.cote, self.cote))
        self.obs.append(pygame.Rect(self.x1, self.y1, self.cote, self.height - self.cote * 2))
        self.obs.append(pygame.Rect(self.x1 + self.width - self.cote * 2, self.y1, self.cote, self.height - self.cote - self.cote))
        nbre = self.nbreObstacle
        i = 0
        while i < nbre:
            while 0 < 9:
                if self.definitionObstacle() == False:
                    break
            i = i + 1

    def constructionSisiny(self,cote,x,y,width,height):
        i = 0
        tabSisiny = []
        tabSisiny.append(pygame.Rect(x,y,width - (cote*3),cote)) # HAUT
        tabSisiny.append(pygame.Rect(x, y  + height - cote*3 , width - (cote*3), cote)) # BAS
        tabSisiny.append(pygame.Rect(x, y, cote, height-cote*2)) # GAUCHE
        tabSisiny.append(pygame.Rect(x + width - cote*3, y, cote,height-cote * 2)) # DROITE
        return tabSisiny

    def definitionObstacle(self):
        x = random.randint(1, int((self.width - self.cote * 4) / self.cote))
        y = random.randint(1, int((self.height - self.cote * 4) / self.cote))
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
    
    def calculer_nombre_obstacles(self, meilleur_score: float = 0) -> int:
        densite = self.calculer_densite_progressive(meilleur_score)
        nb_cases_x = self.width // self.cote
        nb_cases_y = self.height // self.cote
        surface_totale_cases = nb_cases_x * nb_cases_y
        nb_obstacles = int(surface_totale_cases * densite)
        if nb_obstacles < 5: 
            nb_obstacles = 5   # Minimum pour garder du challenge sur petit écran
        elif nb_obstacles > 45: 
            nb_obstacles = 45  # Maximum pour éviter de bloquer complètement le serpent
        return nb_obstacles
    
    def calculer_densite_progressive(self,meilleur_score: int) -> float:
        densite_minimale = 0.02  # 2% d'obstacles pour un vrai débutant (très accessible)
        densite_maximale = 0.06  # 6% d'obstacles maximum (très difficile, style Hardcore)
        
        bonus_difficulte = (meilleur_score // 10) * 0.005
        
        densite_finale = densite_minimale + bonus_difficulte
        
        if densite_finale > densite_maximale:
            densite_finale = densite_maximale
            
        return densite_finale