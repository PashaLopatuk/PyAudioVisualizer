
from math import sqrt
import pygame
from sys import exit

window_size = window_width, window_height  = 1280, 960
pygame.init()
screen = pygame.display.set_mode(window_size)

black = 0, 0, 0
white = 255, 255, 255

def close_action():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

def delay(x):
    pygame.time.delay(x)

def draw(x, h):
    pygame.draw.rect(screen, black, pygame.Rect(x*window_width/24, 0, window_width/24, window_height*sqrt(1-h)))

def fill():
    pygame.display.flip()
    screen.fill(white)