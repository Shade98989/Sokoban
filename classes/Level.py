import pygame
from classes.Player import Player

class Level:
    def __init__(self, player: Player, immovable_objects: pygame.sprite.Group, movable_objects: pygame.sprite.Group, boxspot_objects: pygame.sprite.Group):
        self.__player = player
        self.__immovable_objects = immovable_objects
        self.__movable_objects = movable_objects
        self.__boxspot_objects = boxspot_objects

    def get_player(self):
        return self.__player

    def get_immovables(self):
        return self.__immovable_objects

    def get_movables(self):
        return self.__movable_objects

    def get_boxspots(self):
        return self.__boxspot_objects

    def set_player(self, player: Player):
        self.__player = player