import pygame
from app.utils import isIntersection

class VirtualGamePad:
    
    buttonUpRect = None
    buttonDownRect = None
    buttonLeftRect = None
    buttonRightRect = None

    buttonPauseRect = None
    buttonPayRect = None

    def __init__(self, screen, zoneControlDirection,zonePausePlay):
        self.screen = screen
        self.zoneControlDirection = zoneControlDirection
        self.zonePausePlay = zonePausePlay
        self._initialize_buttons()

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
        center_x = self.zoneControlDirection.centerx
        center_y = self.zoneControlDirection.centery
        button_size = min(self.zoneControlDirection.width, self.zoneControlDirection.height) // 3

        self.buttonUpRect = pygame.Rect(center_x - button_size // 2, center_y - button_size * 1.5, button_size, button_size)
        self.buttonDownRect = pygame.Rect(center_x - button_size // 2, center_y + button_size * 0.5, button_size, button_size)
        self.buttonLeftRect = pygame.Rect(center_x - button_size * 1.5, center_y - button_size // 2, button_size, button_size)
        self.buttonRightRect = pygame.Rect(center_x + button_size * 0.5, center_y - button_size // 2, button_size, button_size)

    def _initialize_buttonsPauseOrPlay(self):
        center_x = self.zonePausePlay.centerx
        center_y = self.zonePausePlay.centery
        button_size = min(self.zonePausePlay.width, self.zonePausePlay.height) // 2

        self.buttonPauseRect = pygame.Rect(center_x - button_size // 2, center_y - button_size // 2, button_size, button_size)
        self.buttonPayRect = self.buttonPauseRect.copy()  # For simplicity, using the same rect for pause and play. You can adjust as needed.

    def _paint_button(self, rect, color = (200, 200, 200)):
        pygame.draw.rect(self.screen, color, rect)

    def draw(self, is_paused=False):
        self._paint_button(self.buttonUpRect)
        self._paint_button(self.buttonDownRect)
        self._paint_button(self.buttonLeftRect)
        self._paint_button(self.buttonRightRect)
        self._paint_pause_play_button(is_paused)

    def _paint_pause_play_button(self, is_paused):
        color = (200, 0, 0) if is_paused else (0, 200, 0)
        self._paint_button(self.buttonPauseRect if is_paused else self.buttonPayRect, color)