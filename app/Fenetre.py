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
        pygame.init()
        SCREEN = pygame.display.set_mode((870, 550))
        pygame.display.set_caption('Snake Bidy')
        pygame.mixer.init()
        SIFFllement = pygame.mixer.music.load("./data/house_lo.ogg")
        pygame.mixer.music.play(100,0.0)
        sonsMaty = pygame.mixer.Sound("./data/punch.wav")
        sonsMinana = pygame.mixer.Sound("./data/whiff.wav")
        sonspause = pygame.mixer.Sound("./data/house_lo.ogg")
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        RED = (255, 0, 0)
        GREEN = (0, 255, 0)
        BLUE = (0, 0, 255)
        LINE = (46,57,44)
        YELLOW = (255, 85, 5)
        cote = 25
        width = 800
        height = 500
        stade = Stade(cote,width,height)
        obs = Obstacle(cote,50,50,width,height)
        serp = Serpent(cote,50 + cote + 100,50 + cote)
        serp2 = Serpent(cote,50 + cote + 100,450)
        serp2.mooveY = -cote
        sak = Sakafo(obs,50,50,width,height,cote,BLUE)
        score = Score(50,25,width,height,BLACK,GREEN)
        gameOver = GameOver(50,50,width,height,cote,WHITE,GREEN,BLACK)
        acceuil = Accueil(50,50,width,height,cote,WHITE,GREEN,RED)
        clock = pygame.time.Clock()
        ac = True
        is_running = True
        while is_running:
            clock.tick(10)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and serp.serp[0].y == serp.serp[1].y:
                        serp.mooveY = -cote
                        serp.mooveX = 0
                    elif event.key == pygame.K_LEFT and serp.serp[0].x == serp.serp[1].x:
                        serp.mooveX = -cote
                        serp.mooveY = 0
                    elif event.key == pygame.K_DOWN and serp.serp[0].y == serp.serp[1].y:
                       serp.demarer = True
                       serp.mooveY = +cote
                       serp.mooveX = 0
                    elif event.key == pygame.K_RIGHT and serp.serp[0].x == serp.serp[1].x:
                        serp.mooveX = +cote
                        serp.mooveY = 0
                    elif event.key == pygame.K_RETURN and serp.demarer == False:
                        serp.demarer = True
                        serp.mooveX = -cote
                        serp.mooveY = 0
                    elif event.key == pygame.K_SPACE:
                        if serp.demarer == True:
                            serp.demarer = False
                            sonspause.play()
                        elif serp.demarer == False:
                            serp.demarer = True
                            sonspause.play()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    xmouse = event.pos[0]
                    ymouse = event.pos[1]
                    a = pygame.Rect(xmouse,ymouse,1,1)
                    b = pygame.Rect(gameOver.textRectButton.x,gameOver.textRectButton.y,gameOver.textRectButton.width,gameOver.textRectButton.height)
                    c = pygame.Rect(acceuil.textRectButton.x,acceuil.textRectButton.y,acceuil.textRectButton.width,acceuil.textRectButton.height)
                    #e = pygame.Rect(score.textRectS.x,score.textRectS.y,score.textRectS.width,score.textRectS.height)
                    if serp.maty == 1 and obs.intersection(a,b) == True:
                        serp.restartSerp()
                        obs.restartObstacle()
                        sak.definitionEmplacement(50,50)
                        pygame.mixer.music.play(100,0.0)
                        sak.score = 0
                    elif ac == True and obs.intersection(a,c):
                        ac = False
            if ac == True:
                stade.dessinStade(SCREEN, LINE)
                acceuil.dessinAcceuil(SCREEN)
            else:
                if serp.maty == 0:
                    serp.midona(obs.obs,sonsMaty)
                    sak.voaHinana(serp,sonsMinana)
                    sak.dessinSakafo(SCREEN)
                    serp.mooveAutomatique()
                    serp.dessinSerpent(SCREEN,RED,GREEN)
                    stade.dessinStade(SCREEN,LINE)
                    obs.dessinObstacle(SCREEN, WHITE)
                elif serp.maty == 1:
                    pygame.mixer.music.stop()
                    stade.dessinStade(SCREEN, LINE)
                    gameOver.afficheGameOver(SCREEN,sak.score)
                score.dessinScore(SCREEN, sak.score)
            pygame.display.update()
            SCREEN.fill(BLACK)
            #musicGame.play()
            time.sleep(0.2)
        pygame.quit()