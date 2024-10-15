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
        self.player = None

    def run(self):
        images = ImageCollection()
        images.load_images()

        pygame.init()
        game_display = pygame.display.set_mode((self.display_width, self.display_height))

        # Game name
        game_name = "SokobanDaWish"
        pygame.display.set_caption(game_name)

        # Initialize game clock
        clock = pygame.time.Clock()

        # Initialize white color
        white = (255, 255, 255)

        # Load the level and player
        self.level_surface = self.level_loader.load_levels()
        self.player = self.level_loader.get_player()

        running = True
        move_distance = 50

        dir = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        self.player._rectangle.y -= move_distance
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        self.player._rectangle.y += move_distance
                    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        self.player._rectangle.x -= move_distance
                        dir = True
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        dir = False
                        self.player._rectangle.x += move_distance

            game_display.blit(self.level_surface, (0, 0))

            if dir:
                game_display.blit(images.PLAYER_LEFT, self.player._rectangle)
            else:
                game_display.blit(images.PLAYER_RIGHT, self.player._rectangle)

            pygame.display.update()

            clock.tick(self.fps)

        pygame.quit()
