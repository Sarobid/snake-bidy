# This is a sample Python script.
import asyncio
import pygame
from app.Fenetre import Fenetre

pygame.init()
fen = Fenetre()
asyncio.run(fen.run())
