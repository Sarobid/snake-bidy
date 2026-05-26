import asyncio
import pygame
import time
from app.Stade import Stade
from app.Obstacle import Obstacle
from app.Serpent import Serpent
from app.Sakafo import Sakafo
from  app.Score import Score
from app.GameOver import GameOver
from app.Accueil import Accueil
from app.VirtualGamePad import VirtualGamePad
from app.utils import calculer_dimensions_jeu, getResteRectBasInRectExtAndRectInt, appliquer_padding_rect, diviser_rect

class Fenetre:

    def __init__(self):
        # pygame.init()
        width, height = self.configurer_ecran(mode="MOBILE")
        self.SCREEN = pygame.display.set_mode((width, height))
        widthScreen, heightScreen = pygame.display.get_surface().get_size()
        pygame.display.set_caption('Snake Bidy')
        pygame.mixer.init()
        # pygame.mixer.music.load("./data/house_lo.ogg")
        # pygame.mixer.music.play(100,0.0)
        self.sonsmaty = pygame.mixer.Sound("./data/punch.wav")
        self.sonsminana = pygame.mixer.Sound("./data/whiff.wav")
        # self.sonspause = pygame.mixer.Sound("./data/house_lo.ogg")
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)
        self.LINE = (46,57,44)
        self.YELLOW = (255, 85, 5)
        self.cote = 17
        # self.width = self.cote * 50
        # self.height = self.cote * 30
        self.pct_g = 0.0
        self.pct_h = 0.2
        self.pct_d = 0.0
        self.pct_b = 0.0
        self.width, self.height = calculer_dimensions_jeu(
            widthScreen, 
            heightScreen, 
            self.cote,
            pct_gauche=self.pct_g,
            pct_droite=self.pct_d,
            pct_haut=self.pct_h,  
            pct_bas=self.pct_b
        )

        self.stade = Stade(self.cote,self.width,self.height,widthScreen,heightScreen,self.pct_g,self.pct_h)
        self.x1 = self.stade.get_xStart()
        self.y1 = self.stade.get_yStart()
        self.virtualGamePad = VirtualGamePad(self.SCREEN,widthScreen,heightScreen,self.stade)
        
        self.serp = Serpent(self.cote,self.x1 + self.cote * 5,self.y1 + self.cote)
        self.score = Score(self.x1,self.y1,self.cote,self.width,self.height,self.BLACK,self.GREEN)
        self.obs = Obstacle(self.cote,self.x1,self.y1,self.width,self.height,self.score.meilleur,self.virtualGamePad)
        self.sak = Sakafo(self.obs,self.x1,self.y1,self.width,self.height,self.cote,self.BLUE)
        self.gameOver = GameOver(self.x1,self.y1,self.width,self.height,self.cote,self.WHITE,self.GREEN,self.BLACK)
        self.acceuil = Accueil(self.x1,self.y1,self.width,self.height,self.cote,self.WHITE,self.GREEN,self.RED)
        self.clock = pygame.time.Clock()
        self.ac = True
        self.is_running = True

    async def run(self):
        while self.is_running:
            self.clock.tick(60)
            self.SCREEN.fill(self.BLACK)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.serp.serp[0].y == self.serp.serp[1].y:
                        self.serp.moveUp()
                    elif event.key == pygame.K_LEFT and self.serp.serp[0].x == self.serp.serp[1].x:
                        self.serp.moveLeft()
                    elif event.key == pygame.K_DOWN and self.serp.serp[0].y == self.serp.serp[1].y:
                       self.serp.moveDown() 
                    elif event.key == pygame.K_RIGHT and self.serp.serp[0].x == self.serp.serp[1].x:
                        self.serp.moveRight()
                    elif event.key == pygame.K_RETURN and self.serp.demarer == False:
                        self.serp.moveLeft()
                    elif event.key == pygame.K_SPACE:
                        self.serp.playOrPause()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    xmouse = event.pos[0]
                    ymouse = event.pos[1]
                    a = pygame.Rect(xmouse,ymouse,1,1)
                    b = pygame.Rect(self.gameOver.textRectButton.x,self.gameOver.textRectButton.y,self.gameOver.textRectButton.width,self.gameOver.textRectButton.height)
                    c = pygame.Rect(self.acceuil.textRectButton.x,self.acceuil.textRectButton.y,self.acceuil.textRectButton.width,self.acceuil.textRectButton.height)
                    #e = pygame.Rect(self.score.textRectS.x,self.score.textRectS.y,self.score.textRectS.width,self.score.textRectS.height)
                    if self.serp.maty == 0:
                        self.virtualGamePad.handle_touch(a, self.serp.moveUp, self.serp.moveDown, self.serp.moveLeft, self.serp.moveRight, self.serp.playOrPause)
                    if self.serp.maty == 1 and self.obs.intersection(a,b) == True:
                        self.serp.restartSerp()
                        self.obs.restartObstacle()
                        self.sak.definitionEmplacement(self.stade.get_xStart(),self.stade.get_yStart())
                        # pygame.mixer.music.play(100,0.0)
                        self.sak.score = 0
                    elif self.ac == True and self.obs.intersection(a,c):
                        self.ac = False
            if self.ac == True:
                self.stade.dessinStade(self.SCREEN, self.LINE)
                self.acceuil.dessinAcceuil(self.SCREEN)

            else:
                if self.serp.maty == 0:
                    # pygame.mixer.music.play(100,0.0)
                    self.serp.midona(self.obs.obs,self.sonsmaty)
                    self.sak.voaHinana(self.serp,self.sonsminana)
                    self.sak.dessinSakafo(self.SCREEN)
                    self.serp.mooveAutomatique()
                    self.serp.dessinSerpent(self.SCREEN,self.RED,self.GREEN)
                    self.stade.dessinStade(self.SCREEN,self.LINE)
                    self.obs.dessinObstacle(self.SCREEN, self.WHITE)
                    self.virtualGamePad.draw(self.serp.demarer)
                elif self.serp.maty == 1:
                    # pygame.mixer.music.stop()
                    self.stade.dessinStade(self.SCREEN, self.LINE)
                    self.gameOver.afficheGameOver(self.SCREEN,self.sak.score)
                    self.obs.set_best_score(self.score.meilleur)
                self.score.dessinScore(self.SCREEN, self.sak.score)

            pygame.display.update()
            #musicGame.play()
            time.sleep(0.2)
            await asyncio.sleep(0) 
        pygame.quit()

    def configurer_ecran(self, mode="PC"):
        """
        Calcule et applique la taille de la fenêtre selon la plateforme cible.
        Retourne un tuple (largeur, hauteur).
        """
        if mode == "MOBILE":
            # Mode Portrait type Smartphone (ex: pour un futur build Android)
            largeur = 800
            hauteur = 400
            
        elif mode == "WEB" or mode == "PC":
            # Mode Web adaptatif : on prend l'espace disponible dans le navigateur
            pygame.display.init()
            info = pygame.display.Info()
            largeur = info.current_w
            hauteur = info.current_h
            
        return largeur, hauteur