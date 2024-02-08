import librosa
import numpy as np

path = "Sound Recordings/crazy_fredrick.wav"
x, sr = librosa.load(path)

left = x.tolist()
right = [0, 0, 0] + x.tolist()

print(left[0:10])
print(right[0:10])