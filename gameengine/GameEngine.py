import pygame
from classes.LevelLoader import LevelLoader
from classes.Level import Level
from classes.ImageCollection import ImageCollection

class GameEngine:

    def __init__(self, display_width, display_height, fps):
        self.display_width = display_width
        self.display_height = display_height
        self.fps = fps
        self.level_loader = LevelLoader()
        self.level_surface = None

    def run(self):
        pygame.init()
        game_display = pygame.display.set_mode((self.display_width, self.display_height))

        # game name
        game_name = "SokobanDaWish"
        pygame.display.set_caption(game_name)

        # initialize game clock
        clock = pygame.time.Clock()

        # initialize white color
        white = (255, 255, 255)

        # paint initial state of screen
        game_display.fill(white)

        # run game
        # TODO

        self.level_surface = self.level_loader.load_levels()

        game_display.blit(self.level_surface, (0, 0))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        print("Move up")
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        print("Move down")
                    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        print("Move left")
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        print("Move right")
            pygame.display.update()
            clock.tick(self.fps)

        pygame.quit()