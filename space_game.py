import pygame

from controls import events_listener, update_screen
from gun import Gun

title = 'Space Invaders'
bg_color = (0, 0, 0)
screens = (700, 800)


def run():
    pygame.init()
    screen = pygame.display.set_mode(screens)
    pygame.display.set_caption(title)
    gun = Gun(screen)
    while True:
        events_listener(gun)
        gun.update_gun()
        update_screen(bg_color, screen, gun)


run()
