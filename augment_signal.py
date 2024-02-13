import librosa
import numpy as np
from scipy.io.wavfile import write

pathSave = "Sound Recordings/altered/"
pathRead = "Sound Recordings/"
filename = "crazy_fredrick.wav"
x_ster, rec_sr = librosa.load(pathRead+filename, mono = False)

def delayAndAttenuateSignal(path, stereo, sr, delay, attenuationFactor):
  period = 1 / sr
  numPaddingZeros = (int) (delay // period) # floor of delay // period
  zeros = [0] * numPaddingZeros

  left = stereo[0].tolist() + zeros # pad to be same length, delay right side
  right = zeros + stereo[1].tolist()
  right = [elem * attenuationFactor for elem in right]

  # make 2d numpy array for stereo write
  stereo_data = np.array([np.asarray(left), np.asarray(right)])
  print(stereo_data.T)
  write(path, sr, stereo_data.T.astype(np.float32))

# Very coarse approximation of 0.5924198ms 
delay = 1 # desired delay in seconds
attenuation = 1 # values to attentuate by for right side TODO use attenuation
delayAndAttenuateSignal(pathSave + filename, x_ster, rec_sr, delay, attenuation)
