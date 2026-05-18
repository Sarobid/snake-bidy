import pygame
import time
from app.Stade import Stade
from app.Obstacle import Obstacle
from app.Serpent import Serpent
from app.Sakafo import Sakafo
from  app.Score import Score

class Fenetre:

    def __init__(self):
        pygame.init()
        SCREEN = pygame.display.set_mode((900, 600))

        pygame.display.set_caption('My Game')

        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        RED = (255, 0, 0)
        GREEN = (0, 255, 0)
        BLUE = (0, 0, 255)
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
        clock = pygame.time.Clock()
        is_running = True
        while is_running:
            clock.tick(60)
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
                       serp.mooveY = +cote
                       serp.mooveX = 0
                    elif event.key == pygame.K_RIGHT and serp.serp[0].x == serp.serp[1].x:
                        serp.mooveX = +cote
                        serp.mooveY = 0
                    #if event.key == pygame.K_w and serp2.serp[0].y == serp2.serp[1].y:
                      #  serp2.mooveY = -cote
                     #   serp2.mooveX = 0
                    #elif event.key == pygame.K_a and serp2.serp[0].x == serp2.serp[1].x:
                      #  serp2.mooveX = -cote
                     #   serp2.mooveY = 0
                    #elif event.key == pygame.K_s and serp2.serp[0].y == serp2.serp[1].y:
                     #  serp2.mooveY = +cote
                     #  serp2.mooveX = 0
                    #elif event.key == pygame.K_d and serp2.serp[0].x == serp2.serp[1].x:
                    #   serp2.mooveX = +cote
                    #    serp2.mooveY = 0
            serp.midona(obs.obs)
            #serp2.midona(obs.obs)
            sak.voaHinana(serp)
            #sak.voaHinana(serp2)
            sak.dessinSakafo(SCREEN)
            serp.mooveAutomatique()
            #serp2.mooveAutomatique()
            obs.dessinObstacle(SCREEN, WHITE)
            serp.dessinSerpent(SCREEN,RED,GREEN)
            #serp2.dessinSerpent(SCREEN, RED, YELLOW)
            stade.dessinStade(SCREEN,WHITE)
            pygame.display.update()
            SCREEN.fill(BLACK)
            score.dessinScore(SCREEN,sak.score)
            time.sleep(0.2)
        pygame.quit()