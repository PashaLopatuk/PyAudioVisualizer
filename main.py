
from fileinput import close
import pygame

from window import close_action, draw, fill, close_action, delay
from audio import notes, levels, second, samp_per_second, song

pygame.init()

frame_counter, index = 0

print(second)

while 1:
    close_action()
    
    for sample in range(second):
        if floor(sample*samp_per_second) in notes:
            index = frame_counter * second / 10
            levels[notes.index(floor(sample*samp_per_second))] = sum([song[index + i] for i in range(-5, 5)])/10 /255
    
    # t = song[counter * 882]
    # t = 50 * t / speed / bit_depth + 5
    for i in range(24):
        draw(i, levels[i])
        # pygame.draw.rect(screen, black, pygame.Rect(32 * i, 0, 32, 400 -levels[i]))

    delay(100)
    # print(t)
    
    fill()
    frame_counter += 1
    levels = [0 for i in range(24)]