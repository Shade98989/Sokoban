import pygame
from classes.Obstacle import Obstacle

class PineTree(Obstacle):
    def __init__(self, surface: pygame.Surface, image: pygame.Surface, rectangle: pygame.Rect):
        super().__init__(surface, image, rectangle)