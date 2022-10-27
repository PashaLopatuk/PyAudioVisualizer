import wave
from json import loads
from settings import settings
from math import floor

locals().update(loads(settings))
song = []

try:
    
    with open(f'{mainPath}\\cache\\{songName[0:-4]}.json', "r") as f:
        song = loads(f.read())
        print('Cache opened!')
except IOError:
    try:
        with open(f'{songPath}\\{songName}', "rb") as f:
            byte = f.read(1)
            while byte:
                byte = f.read(1)
                song.append(int.from_bytes(byte, "big"))
        print('Loaded new song!')
        try:
            
            from json import dumps
            with open(f'{mainPath}\\cache\\{songName[0:-4]}.json', 'w') as f:
                f.write(dumps(song))

            print('Saved cache for new song!')

        except Exception:
            print('Error while saving cache!')

    except IOError:
        print('Error While Opening the file!')

wave_file = wave.open(f'{songPath}\\{songName}', "rb")

sample_rate = wave_file.getframerate()
bit_depth = pow(2, 8) -1
samp_width = wave_file.getsampwidth()
second = sample_rate * samp_width
# second = 44100 * 2
samp_per_second = 1000 / second
polutone = pow(2, 1 / 12)

notes = [82.41 /polutone /polutone /polutone]
levels = [0 for i in range(24)]

for i in range(1, 24):
    notes.append(notes[i-1]*polutone)

notes = list(map(floor, notes))



# print(song[0: 5*second])

# print(song)