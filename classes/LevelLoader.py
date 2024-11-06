import pygame, os
from classes.Player import Player
from classes.PineTree import PineTree
from classes.Box import Box
from classes.BoxSpot import BoxSpot
from classes.ImageCollection import ImageCollection
from classes.Level import Level


class LevelLoader:
    def __init__(self):
        self.__level_map = {}
        self.level_surface = pygame.Surface((500, 500))

    def get_level_count(self):
        return len(self.__level_map)

    def get_level(self):
        return self.__level_map["level1.txt"]

    def __load_level(self, level):
        images = ImageCollection()
        images.load_images()
        file_path = f"collections/{level}"
        with open(file_path, 'r') as file:
            level_data = file.readlines()

        player = None
        movables = pygame.sprite.Group()
        immovables = pygame.sprite.Group()
        boxspots = pygame.sprite.Group()

        player_found = False
        box_count = 0
        boxspot_count = 0

        for y, line in enumerate(level_data):
            line = line.strip()
            if len(line) > 10:
                print(f"Warning: Line {y+1} has more than 10 characters in {file_path}. Ignoring extra characters.")
                line = line[:10]
            elif len(line) < 10:
                print(f"Warning: Line {y+1} has less than 10 characters in {file_path}. Filling with empty spaces.")
                line = line.ljust(10, '_')

            for x, char in enumerate(line):
                position = (x * 50, y * 50)

                object_surface = pygame.Surface((50,50))

                if char == 'p':
                    if player_found:
                        raise ValueError(f"Error: Multiple players found in {file_path} at line {y+1}.")
                    rect = pygame.Rect(x * 50, y * 50, 50, 50)
                    player = Player(object_surface, images.PLAYER_LEFT,rect)
                    self.level_surface.blit(images.LAND, position)
                    player_found = True

                elif char == 'b':
                    rect = pygame.Rect(x * 50, y * 50, 50, 50)
                    box = Box(object_surface, images.BOX,rect)
                    self.level_surface.blit(images.LAND, position)
                    movables.add(box)
                    box_count += 1

                elif char == 's':
                    rect = pygame.Rect(x * 50, y * 50, 50, 50)
                    spot = BoxSpot(object_surface, images.BOXSPOT,rect)
                    self.level_surface.blit(images.BOXSPOT, position)
                    boxspots.add(spot)
                    boxspot_count += 1

                elif char == 'o':
                    rect = pygame.Rect(x * 50, y * 50, 50, 50)
                    obstacle = PineTree(object_surface, images.PINETREE,rect)
                    self.level_surface.blit(images.PINETREE, position)
                    immovables.add(obstacle)

                elif char == '_':
                    self.level_surface.blit(images.LAND, position)

                else:
                    raise ValueError(f"Error: Unrecognized character '{char}' in {file_path} at line {y+1}.")

        if not player:
            raise ValueError(f"Error: Missing player in {file_path}.")
        if box_count == 0:
            raise ValueError(f"Error: No boxes found in {file_path}.")
        if boxspot_count == 0:
            raise ValueError(f"Error: No box spots found in {file_path}.")
        if box_count != boxspot_count:
            raise ValueError(f"Error: Mismatch between number of boxes ({box_count}) and box spots ({boxspot_count}) in {file_path}.")

        self.__level_map[level] = Level(player, immovables, movables, boxspots)

    def load_levels(self):
        levels = os.listdir("collections")
        for level in levels:
            self.__load_level(level)
        return self.level_surface