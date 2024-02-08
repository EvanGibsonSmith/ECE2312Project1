import librosa
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

pathname = "crazy_fredrick.wav"
data, sampling_rate = librosa.load("Sound Recordings/" + pathname, sr = 44000)
freq = librosa.amplitude_to_db(np.abs(librosa.stft(data)), ref=np.max)
print(freq.shape)

# not sure of exact c map from the lecture
# below modified from librosa documentation https://librosa.org/doc/main/auto_examples/plot_display.html
fig, ax = plt.subplots()
img = librosa.display.specshow(freq, x_axis='time', y_axis='linear', cmap='nipy_spectral', ax=ax)
ax.set(title='Spectogram of ' + pathname, ylim=[0, 8000])
fig.colorbar(img, ax=ax, format="%+2.f dB")

plt.show()
