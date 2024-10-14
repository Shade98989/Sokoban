import pygame

class ImageCollection():
    def __init__(self):
        self.BOX = None
        self.BOXSPOT = None
        self.PLAYER_LEFT = None
        self.PLAYER_RIGHT = None
        self.LAND = None
        self.PINETREE = None

    def load_images(self):
        self.BOX = pygame.image.load("images/box.png")
        self.BOXSPOT = pygame.image.load("images/box_spot.png")
        self.PLAYER_LEFT = pygame.image.load("images/fireman_left.png")
        self.PLAYER_RIGHT = pygame.image.load("images/fireman_right.png")
        self.LAND = pygame.image.load("images/land.png")
        self.PINETREE = pygame.image.load("images/pine.png")

        self.BOX = pygame.transform.scale(self.BOX, (50,50))
        self.BOXSPOT = pygame.transform.scale(self.BOXSPOT, (50,50))
        self.PLAYER_LEFT = pygame.transform.scale(self.PLAYER_LEFT, (50,50))
        self.PLAYER_RIGHT = pygame.transform.scale(self.PLAYER_RIGHT, (50,50))
        self.LAND = pygame.transform.scale(self.LAND, (50,50))
        self.PINETREE = pygame.transform.scale(self.PINETREE, (50,50))
