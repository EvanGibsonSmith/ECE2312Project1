import librosa 
import matplotlib.pyplot as plt
import numpy as np

# Look at the discrete number array we got from the audio
path = "Sound Recordings/sound.wav"
x, sr = librosa.load(path)
print("recording shape", x.shape)
print("sampling rate", sr)

# TODO note this doesn't work for some reason (Error in sys.excepthook)
plt.figure(figsize=(14, 5))
librosa.display.waveshow(x, sr=sr)