import pygame
from pygame import image

import logging
import time
from xmlrpc import client

logging.basicConfig(level="DEBUG")

WHITE = (255, 255, 255)

KEY_WIDTH = 110

pygame.init()

class SignalController:
    def __init__(self, xmlrpc_client):
        self.xmlrpc_client = xmlrpc_client
        self.current_direction = ''
        self.dir_to_method = {
            'UP': self.xmlrpc_client.set_up,
            'DOWN': self.xmlrpc_client.set_down,
            'LEFT': self.xmlrpc_client.set_left,
            'RIGHT': self.xmlrpc_client.set_right,
            'UP_LEFT': self.xmlrpc_client.set_up_left,
            'UP_RIGHT': self.xmlrpc_client.set_up_right,
            'DOWN_LEFT': self.xmlrpc_client.set_down_left,
            'DOWN_RIGHT': self.xmlrpc_client.set_down_right,
        }

    def set_direction(self, direction=''):
        if direction == self.current_direction:
            return

        if self.current_direction:
            self.dir_to_method[self.current_direction](False)

        if direction:
            self.dir_to_method[direction](True)

        self.current_direction = direction

class ArrowSprite:
    def __init__(self, key_up_img, key_down_img, draw_location):
        super().__init__()

        self.key_up_img = image.load(key_up_img).convert()
        self.key_up_img.set_colorkey(WHITE)

        self.key_down_img = image.load(key_down_img).convert()
        self.key_down_img.set_colorkey(WHITE)

        self.draw_location = draw_location

    def draw(self, screen, active=False):
        if active:
            image = self.key_down_img
        else:
            image = self.key_up_img

        screen.blit(image, self.draw_location)


def draw_key_sprites(screen, key_sprites, active_keys=None):
    if not active_keys:
        active_keys = []

    for direction, sprite in key_sprites.items():
        if direction in active_keys:
            sprite.draw(screen, active=True)
        else:
            sprite.draw(screen, active=False)

size = (640, 400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('RC Remote Controller')

key_sprites = {
    "UP": ArrowSprite('key_sprites/key_up.png', 'key_sprites/key_up_pressed.png',
                      (size[0] / 2 - KEY_WIDTH / 2, size[1] / 2 - KEY_WIDTH)),
    "DOWN": ArrowSprite('key_sprites/key_down.png', 'key_sprites/key_down_pressed.png',
                        (size[0] / 2 - KEY_WIDTH / 2, size[1] / 2)),
    "RIGHT": ArrowSprite('key_sprites/key_right.png', 'key_sprites/key_right_pressed.png',
                         (size[0] / 2 + KEY_WIDTH / 2, size[1] / 2)),
    "LEFT": ArrowSprite('key_sprites/key_left.png', 'key_sprites/key_left_pressed.png',
                        (size[0] / 2 - KEY_WIDTH * 3 / 2, size[1] / 2))
}

carry_on = True
clock = pygame.time.Clock()

xmlrpc_client = client.ServerProxy('http://localhost:8080')
signal_controller = SignalController(xmlrpc_client)

while carry_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carry_on = False

    screen.fill((255, 255, 255))

    keys = pygame.key.get_pressed()
    active_keys = []
    if keys[pygame.K_UP]:
        active_keys.append('UP')
    if keys[pygame.K_DOWN]:
        active_keys.append('DOWN')
    if keys[pygame.K_LEFT]:
        active_keys.append('LEFT')
    if keys[pygame.K_RIGHT]:
        active_keys.append('RIGHT')

    if 'UP' in active_keys and 'RIGHT' in active_keys:
        signal_controller.set_direction('UP_RIGHT')
    elif 'UP' in active_keys and 'LEFT' in active_keys:
        signal_controller.set_direction('UP_LEFT')
    elif 'DOWN' in active_keys and 'RIGHT' in active_keys:
        signal_controller.set_direction('DOWN_RIGHT')
    elif 'DOWN' in active_keys and 'LEFT' in active_keys:
        signal_controller.set_direction('DOWN_LEFT')
    elif 'UP' in active_keys:
        signal_controller.set_direction('UP')
    elif 'DOWN' in active_keys:
        signal_controller.set_direction('DOWN')
    elif 'RIGHT' in active_keys:
        signal_controller.set_direction('RIGHT')
    elif 'LEFT' in active_keys:
        signal_controller.set_direction('LEFT')
    else:
        signal_controller.set_direction('')

    draw_key_sprites(screen=screen, key_sprites=key_sprites, active_keys=active_keys)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
