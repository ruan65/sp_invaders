import pygame
from pygame.sprite import Group

from constants import screen_size, title, bg_color
from controls import events_listener, update_screen, update_bullets, create_army  # , create_army
from gun import Gun


def run():
    pygame.init()
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption(title)
    gun = Gun(screen)
    bullets = Group()
    army = Group()
    create_army(screen, army)

    while True:
        events_listener(screen, gun, bullets)
        gun.update_gun()
        update_screen(bg_color, screen, gun, bullets, army)
        update_bullets(bullets)


run()
