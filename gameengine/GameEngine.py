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

                # Calculate new position based on input but don't move the player yet
                new_x, new_y = self.player.rect.x, self.player.rect.y

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        new_y -= move_distance
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        new_y += move_distance
                    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        new_x -= move_distance
                        dir = True
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        new_x += move_distance
                        dir = False

                # Create a new rectangle with the intended new position
                new_rect = pygame.Rect(new_x, new_y, self.player.rect.width, self.player.rect.height)

                # Check for collisions with immovable obstacles
                obstacle_collision = False
                level = self.level_loader.get_level()  # Get the specific level object
                for obstacle in level.get_immovables():
                    if new_rect.colliderect(obstacle.rect):  # Check if new position collides with any obstacle
                        obstacle_collision = True
                        break

                # Move the player if no collision is detected
                if not obstacle_collision:
                    self.player.rect.x = new_x
                    self.player.rect.y = new_y

            # Clear and redraw the level and player
            game_display.blit(self.level_surface, (0, 0))

            if dir:
                game_display.blit(images.PLAYER_LEFT, self.player.rect)
            else:
                game_display.blit(images.PLAYER_RIGHT, self.player.rect)

            # Update the display
            pygame.display.update()

            # Cap the frame rate
            clock.tick(self.fps)

        pygame.quit()
