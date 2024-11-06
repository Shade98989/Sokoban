import pygame
from classes.StepableObject import StepableObject

class BoxSpot(StepableObject):
    def __init__(self, surface: pygame.Surface, image: pygame.Surface, rectangle: pygame.Rect, contains_box: bool = False):
        super().__init__(surface, image, rectangle)

        self.rect = rectangle