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
# Also coarse approximation of 0.1778/343 = 0.5183667 ms
# Average head delay = 0.55539325 ms
avg_head = 0.00055539325 #in seconds
# desired delay in seconds
delay1 = [avg_head, 0.001] # the values that have different attenuations
delay2 = [0.010, 0.100] # the values that have no attenuation
attenuation = [1.5, 3, 6] # values to attentuate by for right side TODO use attenuation


for d in delay1:
  for a in attenuation:
    filename = str(d) + "delay-" + str(a) + "dB-" + filename
    delayAndAttenuateSignal(pathSave + filename, x_ster, rec_sr, d, a/6)

for d in delay2:
  filename = str(d) + "delay-" + "6dB-" + filename
  delayAndAttenuateSignal(pathSave + filename, x_ster, rec_sr, d, 1)
