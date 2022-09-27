from ctypes import sizeof
from random import sample
from re import X
from tkinter import Frame
from turtle import delay
import wave
from math import floor, sqrt
import json, pygame, sys

# from time import sleep

rpath = "D:/downloads/Nirvana - Heart Shaped Box [MULTITRACK]/"
file_path = 'Nirvana Heart Shaped Box Guitar.wav'

file = wave.open(f'{rpath}{file_path}', 'rb')

sample_rate = 44100 # file.getframerate()
bit_depth = pow(2, 8) -1
samp_width = file.getsampwidth()
second = sample_rate * samp_width

# frames = file.readframes(file.getnframes())

print(sample_rate)
print('samp lenght ',file.getsampwidth())

song = []

# try:
#     with open(f'{rpath}{file_path}', "rb") as f:
#         byte = f.read(1)
#         while byte:
#             # Do stuff with byte.
#             byte = f.read(1)
#             song.append(int.from_bytes(byte, "big"))
# except IOError:
#      print('Error While Opening the file!')

# with open('d:/musorka2/song encoded.json', 'w') as f:
#     f.write(json.dumps(song [4 * second : 24 * second]))

# print('Success!')


with open('d:/musorka2/song encoded.json', 'r') as f:
    song = json.loads(f.read())

# print(song)

pygame.init()

size = width, height = 640, 400
speed = [2, 2]
black = 0, 0, 0
white = 255, 255, 255

screen = pygame.display.set_mode(size)

counter = t = 0
fps = 10
speed = floor(second / fps / 10)
frame_speed = floor(1000 / fps)
polutone = pow(2, 1 / 12)
tone = pow(2, 1 / 6)
co = 1000 / speed
k = 0

# notes = [float(f'{82.41 /polutone /polutone /polutone:.2f}')]
notes = [floor(82.41 /polutone /polutone /polutone)]
levels = [0 for i in range(24)]
for i in range(1, 24):
    # notes.append(float(f'{notes[i-1]*polutone:.2f}'))
    notes.append(floor(notes[i-1]*polutone))

print('While')
print(notes)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    for i in range(speed-1):
        print(i)
        t += song[counter * speed + i]

        if floor(i * co) in notes:
            k = notes.index(floor(i * co))
            # levels[k] = song[counter * speed + i]
            # levels[k] += song[counter * speed + i-1]
            # levels[k] += song[counter * speed + i+1]
            # levels[k] = levels[k] / 255 * 400 /3
            levels[k] =  song[counter * speed + i-4] + song[counter * speed + i-3] + song[counter * speed + i-2]+ song[counter * speed + i-1] + song[counter * speed + i] + song[counter * speed + i+1] + song[counter * speed + i+2] + song[counter * speed + i+3]
            levels[k] = pow(levels[k], 0.6)
    
    # t = song[counter * 882]
    t = 50 * t / speed / bit_depth + 5
    for i in range(24):

        pygame.draw.rect(screen, black, pygame.Rect(32 * i, 0, 32, 400 -levels[i]))

    pygame.time.delay(frame_speed)
    # print(t)
    
    pygame.display.flip()
    screen.fill(white)
    counter += 1
    levels = [0 for i in range(24)]