import pygame
from pygame.sprite import Group

from controls import events_listener, update_screen, update_bullets
from gun import Gun
from ino import Ino

title = 'Space Invaders'
bg_color = (0, 0, 0)
screens = (700, 800)


def run():
    pygame.init()
    screen = pygame.display.set_mode(screens)
    pygame.display.set_caption(title)
    gun = Gun(screen)
    bullets = Group()
    ino = Ino(screen)

    while True:
        events_listener(screen, gun, bullets)
        gun.update_gun()
        update_screen(bg_color, screen, gun, ino, bullets)
        update_bullets(bullets)

run()
