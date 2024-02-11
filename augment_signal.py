import librosa
import numpy as np

path = "Sound Recordings/crazy_fredrick.wav"
x, sr = librosa.load(path)

attenuation = [0.25, 0.5, 1.0]

#Sampling rate: 44100 Hz --> T = 0.0227 ms
for i in range(0,3)
  delay = 10^i
  delayNum = (int)(delay/0.0227)
  zeros = [0]*delayNum
  left = x.tolist() + zeros
  right = zeros + x.tolist()

  name = "Sound Recordings/crazy_fredrick" + str(delay) + "ms-"

  for a in attenuation
    right = a*right
    name = name + str(a*6) + "dB.wav"
  


#print(left[0:10])
#print(right[0:10])
