
import pygame

# from window import close_action, draw, fill, close_action, delay
from audio import notes, levels, second, samp_per_second, song


from sys import exit
from math import floor
from settings import settings
from json import loads
locals().update(loads(settings))

pygame.display.set_caption("PyAudioVisualizer")

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
    pygame.draw.rect(screen, black, pygame.Rect(x*window_width/24, 0, window_width/24, window_height*(1-h)))

def fill():
    pygame.display.flip()
    screen.fill(white)

frame_counter = index = 0

# print(second)
# print(song)


pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound(f'{songPath}\\{songName}')
# pygame.mixer.music.set_volume(0.5)
sound.play()



while 1:
    close_action()
    
    for sample in range(0, second, 4):
        # print(floor(sample*samp_per_second))
        if floor(sample*samp_per_second) in notes:
            index = floor(frame_counter * second / 10) + sample
            # print(index)
            # levels[notes.index(floor(sample*samp_per_second))] += sum([song[index + i] for i in range(-5, 5)])/100 /255
            levels[notes.index(floor(sample*samp_per_second))] = song[index] /255
            # print(song[index])
            # print((notes.index(floor(sample*samp_per_second))))
            
            # draw(notes.index(floor(sample*samp_per_second)), song[index] /255)
    # print(levels)

    
    for i in range(24):
        draw(i, levels[i])
       
    delay(100)
    
    
    fill()
    frame_counter += 1
    levels = [0 for i in range(24)]
    # levels = list(map(lambda x : x / 50, levels))
    # levels = [levels[i] / 100 for i in range(24)]