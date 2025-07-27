import pygame
from pygame.sprite import Group, Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Alien(Sprite):
    def __init__(self, game: 'AlienInvasion', x, y):
        super().__init__()

        self.screen = game.screen
        self.settings = game.settings
        self.boundaries = game.screen.get_rect()

        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(
        self.image, (self.settings.alien_w, self.settings.alien_h)
        )
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.y = self.rect.y

    def update(self):
        pass

    def draw_alien(self):
        self.screen.blit(self.image, self.rect)