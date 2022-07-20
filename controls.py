import pygame
import sys


def events_listener(gun):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if is_right_key(event):
                gun.move_right = True
            elif is_left_key(event):
                gun.move_left = True
        elif event.type == pygame.KEYUP:
            if is_right_key(event):
                gun.move_right = False
            elif is_left_key(event):
                gun.move_left = False


def is_right_key(event):
    return event.key == pygame.K_d or event.key == pygame.K_RIGHT


def is_left_key(event):
    return event.key == pygame.K_a or event.key == pygame.K_LEFT


def update_screen(bg_color, screen, gun):
    screen.fill(bg_color)
    gun.rander()
    pygame.display.flip()
