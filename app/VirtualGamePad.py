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
        color = (200, 0, 0) if is_paused else (0, 200, 0)
        self._paint_button(self.buttonPauseRect if is_paused else self.buttonPayRect, color)