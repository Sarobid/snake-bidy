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

class Fenetre:

    def __init__(self):
        # pygame.init()
        self.SCREEN = pygame.display.set_mode((870, 550))
        pygame.display.set_caption('Snake Bidy')
        pygame.mixer.init()
        pygame.mixer.music.load("./data/house_lo.ogg")
        pygame.mixer.music.play(100,0.0)
        self.sonsmaty = pygame.mixer.Sound("./data/punch.wav")
        self.sonsminana = pygame.mixer.Sound("./data/whiff.wav")
        self.sonspause = pygame.mixer.Sound("./data/house_lo.ogg")
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)
        self.LINE = (46,57,44)
        self.YELLOW = (255, 85, 5)
        self.cote = 15
        self.width = self.cote * 50
        self.height = self.cote * 30

        self.stade = Stade(self.cote,self.width,self.height)
        self.x1 = self.stade.get_xStart()
        self.y1 = self.stade.get_yStart()
        self.obs = Obstacle(self.cote,self.x1,self.y1,self.width,self.height)
        self.serp = Serpent(self.cote,self.x1 + self.cote * 5,self.y1 + self.cote)
        self.sak = Sakafo(self.obs,self.x1,self.y1,self.width,self.height,self.cote,self.BLUE)
        self.score = Score(self.x1,self.cote,self.width,self.height,self.BLACK,self.GREEN)
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
                        self.serp.demarer = True
                        self.serp.mooveY = -self.cote
                        self.serp.mooveX = 0
                    elif event.key == pygame.K_LEFT and self.serp.serp[0].x == self.serp.serp[1].x:
                        self.serp.demarer = True
                        self.serp.mooveX = -self.cote
                        self.serp.mooveY = 0
                    elif event.key == pygame.K_DOWN and self.serp.serp[0].y == self.serp.serp[1].y:
                       self.serp.demarer = True
                       self.serp.mooveY = +self.cote
                       self.serp.mooveX = 0
                    elif event.key == pygame.K_RIGHT and self.serp.serp[0].x == self.serp.serp[1].x:
                        self.serp.demarer = True
                        self.serp.mooveX = +self.cote
                        self.serp.mooveY = 0
                    elif event.key == pygame.K_RETURN and self.serp.demarer == False:
                        self.serp.demarer = True
                        self.serp.mooveX = -self.cote
                        self.serp.mooveY = 0
                    elif event.key == pygame.K_SPACE:
                        if self.serp.demarer == True:
                            self.serp.demarer = False
                            # self.sonspause.play()
                        elif self.serp.demarer == False:
                            self.serp.demarer = True
                            # self.sonspause.play()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    xmouse = event.pos[0]
                    ymouse = event.pos[1]
                    a = pygame.Rect(xmouse,ymouse,1,1)
                    b = pygame.Rect(self.gameOver.textRectButton.x,self.gameOver.textRectButton.y,self.gameOver.textRectButton.width,self.gameOver.textRectButton.height)
                    c = pygame.Rect(self.acceuil.textRectButton.x,self.acceuil.textRectButton.y,self.acceuil.textRectButton.width,self.acceuil.textRectButton.height)
                    #e = pygame.Rect(self.score.textRectS.x,self.score.textRectS.y,self.score.textRectS.width,self.score.textRectS.height)
                    if self.serp.maty == 1 and self.obs.intersection(a,b) == True:
                        self.serp.restartSerp()
                        self.obs.restartObstacle()
                        self.sak.definitionEmplacement(self.stade.get_xStart(),self.stade.get_yStart())
                        pygame.mixer.music.play(100,0.0)
                        self.sak.score = 0
                    elif self.ac == True and self.obs.intersection(a,c):
                        self.ac = False
            if self.ac == True:
                self.stade.dessinStade(self.SCREEN, self.LINE)
                self.acceuil.dessinAcceuil(self.SCREEN)
            else:
                if self.serp.maty == 0:
                    self.serp.midona(self.obs.obs,self.sonsmaty)
                    self.sak.voaHinana(self.serp,self.sonsminana)
                    self.sak.dessinSakafo(self.SCREEN)
                    self.serp.mooveAutomatique()
                    self.serp.dessinSerpent(self.SCREEN,self.RED,self.GREEN)
                    self.stade.dessinStade(self.SCREEN,self.LINE)
                    self.obs.dessinObstacle(self.SCREEN, self.WHITE)
                elif self.serp.maty == 1:
                    pygame.mixer.music.stop()
                    self.stade.dessinStade(self.SCREEN, self.LINE)
                    self.gameOver.afficheGameOver(self.SCREEN,self.sak.score)
                self.score.dessinScore(self.SCREEN, self.sak.score)
            pygame.display.update()
            #musicGame.play()
            time.sleep(0.2)
            await asyncio.sleep(0) 
        pygame.quit()