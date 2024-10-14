import pygame


class GameObject(pygame.sprite.Sprite):
    def __init__(self, surface: pygame.Surface, image: pygame.Surface, rectangle: pygame.Rect):
        pygame.sprite.Sprite.__init__(self)
        self._surface = surface
        self._image = image
        self._rectangle = rectangle

        # other attributes

    def get_surface(self):
        return self._surface

    def get_rectangle(self):
        return self._rectangle

    def get_image(self):
        return self._image

    def set_image(self, image):
        self._image = image

    def update(self):
        pass
    # other methods
