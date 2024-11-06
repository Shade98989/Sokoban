import pygame
from classes.MovableObject import MovableObject

class Box(MovableObject):
    def __init__(self, surface: pygame.Surface, image: pygame.Surface, rectangle: pygame.Rect):
        super().__init__(surface, image, rectangle)

        self.rect = rectangle

    def get_rect(self):
        return self._rectangle
