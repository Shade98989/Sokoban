import sys
import pygame
import os
import time
from classes.LevelLoader import LevelLoader
from classes.ImageCollection import ImageCollection

class GameEngine:

    def __init__(self, display_width, display_height, fps):
        self.display_width = display_width
        self.display_height = display_height
        self.fps = fps
        self.level_loader = LevelLoader()
        self.level_surface = None
        self.level_num = 1
        self.moves = 0
        self.level_start_time = 0

    def save_level_stats(self):
        directory = "lastruns"

        if not os.path.exists(directory):
            os.makedirs(directory)

        filename = os.path.join(directory, f"last_run_level{self.level_num}.txt")

        time_taken = int(time.time() - self.level_start_time)

        with open(filename, 'w') as file:
            file.write(f"moves: {self.moves}\n")
            file.write(f"time: {time_taken} seconds\n")

    def check_win_condition(self):
        level = self.level_loader.get_level("level" + str(self.level_num) + ".txt")
        boxes_on_spots = 0

        for box in level.get_movables():
            for spot in level.get_boxspots():
                if box.get_rect().colliderect(spot.rect):
                    boxes_on_spots += 1

        return boxes_on_spots == len(level.get_movables())

    def run(self):
        images = ImageCollection()
        images.load_images()

        pygame.init()
        game_display = pygame.display.set_mode((self.display_width, self.display_height))

        game_name = "SokobanDaWish"
        pygame.display.set_caption(game_name)

        clock = pygame.time.Clock()

        running = True
        move_distance = 50

        direction = True

        while running:

            self.level_surface = self.level_loader.load_levels(f"level{self.level_num}.txt")
            level = self.level_loader.get_level(f"level{self.level_num}.txt")

            level_running = True

            self.moves = 0
            self.level_start_time = time.time()

            while level_running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    new_x, new_y = level.get_player().rect.x, level.get_player().rect.y
                    player_initial_x, player_initial_y = level.get_player().rect.x, level.get_player().rect.y

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP or event.key == pygame.K_w:
                            new_y -= move_distance
                        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                            new_y += move_distance
                        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                            new_x -= move_distance
                            direction = True
                        elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                            new_x += move_distance
                            direction = False

                    new_rect = pygame.Rect(new_x, new_y, level.get_player().rect.width, level.get_player().rect.height)

                    obstacle_collision = False
                    for obstacle in level.get_immovables():
                        if new_rect.colliderect(obstacle.rect):
                            obstacle_collision = True
                            break

                    for box in level.get_movables():
                        if new_rect.colliderect(box.rect):

                            box_new_x, box_new_y = box.rect.x, box.rect.y

                            if event.key == pygame.K_UP or event.key == pygame.K_w:
                                box_new_y -= move_distance
                            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                                box_new_y += move_distance
                            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                                box_new_x -= move_distance
                            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                                box_new_x += move_distance

                            new_box_rect = pygame.Rect(box_new_x, box_new_y, box.rect.width, box.rect.height)

                            box_blocked = False
                            for obstacle in level.get_immovables():
                                if new_box_rect.colliderect(obstacle.rect):
                                    box_blocked = True
                                    break

                            if not (0 <= box_new_x < 500 and 0 <= box_new_y < 500):
                                obstacle_collision = True
                                break

                            for other_box in level.get_movables():
                                if other_box != box and new_box_rect.colliderect(other_box.rect):
                                    box_blocked = True
                                    break

                            if not box_blocked:
                                box.rect.x = box_new_x
                                box.rect.y = box_new_y
                            else:
                                obstacle_collision = True

                    if not obstacle_collision:
                        if 0 <= new_x < 500 and 0 <= new_y < 500:
                            level.get_player().rect.x = new_x
                            level.get_player().rect.y = new_y

                            if (level.get_player().rect.x, level.get_player().rect.y) != (player_initial_x, player_initial_y):
                                self.moves += 1

                game_display.blit(self.level_surface, (0, 0))

                if direction:
                    game_display.blit(images.PLAYER_LEFT, level.get_player().rect)
                else:
                    game_display.blit(images.PLAYER_RIGHT, level.get_player().rect)

                for box in level.get_movables():
                    game_display.blit(images.BOX, box.rect)

                if self.check_win_condition():
                    self.save_level_stats()
                    level_running = False
                    self.level_num += 1
                    if not os.path.exists(f"collections/level{self.level_num}.txt"):
                        pygame.quit()
                        sys.exit()

                pygame.display.update()

                clock.tick(self.fps)

        pygame.quit()
