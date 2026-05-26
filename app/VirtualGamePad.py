import pygame
from app.utils import isIntersection
from app.utils import appliquer_padding_rect, diviser_rect , positionnerRectZCentreVerticalementAGauche,positionnerRectZCentreVerticalementADroite


class VirtualGamePad:
    
    buttonUpRect = None
    buttonDownRect = None
    buttonLeftRect = None
    buttonRightRect = None

    buttonPauseRect = None
    buttonPayRect = None
    zoneControlDirection = None
    zonePausePlay = None

    def __init__(self, screen,widthScreen, heightScreen, stade):
        self.screen = screen
        self.stade = stade
        self.widthScreen = widthScreen
        self.heightScreen = heightScreen
        self._definition_zone_control()
        self._initialize_buttons()

    def _definition_zone_control(self):
        screenRect = pygame.Rect(0, 0, self.widthScreen, self.heightScreen)
        stadeRect = pygame.Rect(self.stade.get_xStart(), self.stade.get_yStart(), self.stade.width, self.stade.height)
        heightZoneControl = self.stade.cote * 6
        widthZoneControl = heightZoneControl
        rectZoneControl = pygame.Rect(0, 0, widthZoneControl, heightZoneControl)
        self.zonePausePlay = positionnerRectZCentreVerticalementAGauche(screenRect, stadeRect, rectZoneControl.copy())
        self.zoneControlDirection = positionnerRectZCentreVerticalementADroite(screenRect, stadeRect, rectZoneControl.copy())
       
    
    def _draw_zone_control(self):
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        pygame.draw.rect(self.screen, WHITE, self.zoneControlDirection)
        pygame.draw.rect(self.screen, WHITE, self.zonePausePlay)
        pygame.draw.rect(self.screen, BLACK, self.zoneControlDirectionPaddingCote)
        pygame.draw.rect(self.screen, BLACK, self.zonePausePlayPaddingCote)



    def handle_touch(self, mouseRect, moveUp, moveDown, moveLeft, moveRight, playOrPause):
        if isIntersection(mouseRect, self.buttonUpRect):
            moveUp()
        elif isIntersection(mouseRect, self.buttonDownRect):
            moveDown()
        elif isIntersection(mouseRect, self.buttonLeftRect):
            moveLeft()
        elif isIntersection(mouseRect, self.buttonRightRect):
            moveRight()
        elif isIntersection(mouseRect, self.buttonPauseRect):
            playOrPause()
        elif isIntersection(mouseRect, self.buttonPayRect):
            playOrPause()
        return None

    def _initialize_buttons(self):
        self._initialize_buttonsControlDirection()
        self._initialize_buttonsPauseOrPlay()

    def _initialize_buttonsControlDirection(self):
        zoneControlDirectionPaddingCote = appliquer_padding_rect(self.zoneControlDirection.copy(), self.stade.cote)
        center_x = zoneControlDirectionPaddingCote.centerx
        center_y = zoneControlDirectionPaddingCote.centery
        button_size = min(zoneControlDirectionPaddingCote.width, zoneControlDirectionPaddingCote.height) // 3
        self.zoneControlDirectionPaddingCote = zoneControlDirectionPaddingCote
        self.buttonUpRect = pygame.Rect(center_x - button_size // 2, center_y - button_size * 1.5, button_size, button_size)
        self.buttonDownRect = pygame.Rect(center_x - button_size // 2, center_y + button_size * 0.5, button_size, button_size)
        self.buttonLeftRect = pygame.Rect(center_x - button_size * 1.5, center_y - button_size // 2, button_size, button_size)
        self.buttonRightRect = pygame.Rect(center_x + button_size * 0.5, center_y - button_size // 2, button_size, button_size)

    def _initialize_buttonsPauseOrPlay(self):
        zonePausePlayPaddingCote = appliquer_padding_rect(self.zonePausePlay.copy(), self.stade.cote)
        center_x = zonePausePlayPaddingCote.centerx
        center_y = zonePausePlayPaddingCote.centery
        button_size = min(zonePausePlayPaddingCote.width, zonePausePlayPaddingCote.height) // 2
        self.zonePausePlayPaddingCote = zonePausePlayPaddingCote
        self.buttonPauseRect = pygame.Rect(center_x - button_size // 2, center_y - button_size // 2, button_size, button_size)
        self.buttonPayRect = self.buttonPauseRect.copy()  # For simplicity, using the same rect for pause and play. You can adjust as needed.

    def _paint_button(self, rect, color = (200, 200, 200)):
        pygame.draw.rect(self.screen, color, rect)

    def draw(self, is_paused=False):
        self._draw_zone_control()
        self._paint_button(self.buttonUpRect)
        self._paint_button(self.buttonDownRect)
        self._paint_button(self.buttonLeftRect)
        self._paint_button(self.buttonRightRect)
        self._paint_pause_play_button(is_paused)


    def _paint_pause_play_button(self, is_paused):
        rect = self.buttonPauseRect if is_paused else self.buttonPayRect
        FOND_BOUTON       = (45, 50, 60)      
        LUMIERE_BORD      = (90, 100, 115)    
        OMBRE_BORD        = (20, 22, 26)      
        
        COULEUR_PLAY      = (50, 255, 50)     
        COULEUR_PAUSE     = (255, 50, 50)     
        
        pygame.draw.rect(self.screen, FOND_BOUTON, rect)
        
        pygame.draw.line(self.screen, LUMIERE_BORD, rect.topleft, rect.topright, 2)
        pygame.draw.line(self.screen, LUMIERE_BORD, rect.topleft, rect.bottomleft, 2)
        pygame.draw.line(self.screen, OMBRE_BORD, rect.bottomleft, rect.bottomright, 2)
        pygame.draw.line(self.screen, OMBRE_BORD, rect.topright, rect.bottomright, 2)

        centre_x, centre_y = rect.center
        max_largeur = int(rect.width * 0.8)
        max_hauteur = int(rect.height * 0.8)

        if not is_paused:
            sommet_gauche_haut = (centre_x - max_largeur // 2, centre_y - max_hauteur // 2)
            sommet_gauche_bas  = (centre_x - max_largeur // 2, centre_y + max_hauteur // 2)
            pointe_droite      = (centre_x + max_largeur // 2, centre_y)
            
            pygame.draw.polygon(self.screen, COULEUR_PLAY, [sommet_gauche_haut, sommet_gauche_bas, pointe_droite])
            
        else:
            largeur_barre = int(max_largeur * 0.33)
            barre_gauche_rect = pygame.Rect(
                centre_x - max_largeur // 2,
                centre_y - max_hauteur // 2,
                largeur_barre,
                max_hauteur
            )
            barre_droite_rect = pygame.Rect(
                centre_x + max_largeur // 2 - largeur_barre,
                centre_y - max_hauteur // 2,
                largeur_barre,
                max_hauteur
            )
            
            pygame.draw.rect(self.screen, COULEUR_PAUSE, barre_gauche_rect)
            pygame.draw.rect(self.screen, COULEUR_PAUSE, barre_droite_rect)