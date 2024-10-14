import pygame
from classes.GameObject import GameObject

class StepableObject(GameObject):
    def __init__(self, surface: pygame.Surface, image: pygame.Surface, rectangle: pygame.Rect):
        super().__init__(surface, image, rectangle)