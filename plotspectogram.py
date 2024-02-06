import librosa
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

pathname = "crazy_fredrick.wav"
data, sampling_rate = librosa.load("Sound Recordings/" + pathname, sr = 44000)
freq = librosa.amplitude_to_db(np.abs(librosa.stft(data)), ref=np.max)
print(freq.shape)

# not sure of exact c map from the lecture
librosa.display.specshow(freq, cmap='nipy_spectral') 
plt.show()