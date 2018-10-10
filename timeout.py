# Camera module will keep track of sprite offset.

# Show a dialog when time is out.
from loader import load_image
import pygame
from pygame.locals import *

NOTE_HALF_X = 500
NOTE_HALF_Y = 500


# Alert body.
class Alert(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image('over.png')
        self.rect = self.image.get_rect()
        self.x = int(pygame.display.Info().current_w / 2) - NOTE_HALF_X
        self.y = int(pygame.display.Info().current_h / 2) - NOTE_HALF_Y
        self.rect.topleft = self.x, self.y




