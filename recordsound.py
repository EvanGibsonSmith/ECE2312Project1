# MODIFIED CODE FROM CLASS https://github.com/BASHLab/ECE2312/blob/main/Lecture%20Codes/lecture1.ipynb
# import necessary modules
import sounddevice as sd
from scipy.io.wavfile import write


pathname = "crazy_fredrick.wav"
# Define Sampling Rate or Frequency in Hz
sr = 44100

# Record duration in seconds
duration = 5

# Start audio recording
recording = sd.rec(int(duration*sr), samplerate=sr, channels=2) # we will record with a  mono or stereo channel microphone

# Record audio for the given duration
print("recording...............")
sd.wait()

# Write it to a file
path = "Sound Recordings/" + pathname
write(path, sr, recording)