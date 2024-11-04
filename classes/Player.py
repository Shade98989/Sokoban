import pygame
from classes.MovableObject import MovableObject


class Player(MovableObject):
    def __init__(self, surface: pygame.Surface, image: pygame.Surface, rectangle: pygame.Rect):
        super().__init__(surface, image, rectangle)

        self.rect = rectangle

        self.__score = 0
        self.__move_count = 0

    def get_score(self):
        return self.__score

    def get_moves(self):
        return self.__move_count