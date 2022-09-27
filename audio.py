import wave
from json import loads
from settings import settings
from math import floor

locals().update(loads(settings))
song = []

try:
    
    with open(f'cache\\{songPath}\\{songName}', "r") as f:
        song = loads(f.read())
except IOError:
    try:
        with open(f'{songPath}\\{songName}', "rb") as f:
            byte = f.read(1)
            while byte:
                byte = f.read(1)
                song.append(int.from_bytes(byte, "big"))
    except IOError:
        print('Error While Opening the file!')

print(song)

wave_file = wave.open(f'{songPath}\\{songName}', "rb")

sample_rate = wave_file.getframerate()
bit_depth = pow(2, 8) -1
samp_width = wave_file.getsampwidth()
second = sample_rate * samp_width
samp_per_second = 1000 / second
polutone = pow(2, 1 / 12)

notes = [82.41 /polutone /polutone /polutone]
levels = [0 for i in range(24)]

for i in range(1, 24):
    notes.append(notes[i-1]*polutone)

notes = map(floor, notes)

