import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

audio_file = "01_xiaoyaoxian-opencpop.wav"
y, sr = librosa.load(audio_file)

mel_spectrogram = librosa.feature.melspectrogram(y=y, sr=sr)

mel_spectrogram_db = librosa.power_to_db(mel_spectrogram, ref=np.max)

plt.figure(figsize=(10, 4))
librosa.display.specshow(mel_spectrogram_db, x_axis="time", y_axis="mel")
plt.colorbar(format="%+2.0f dB")
plt.title("Mel Spectrogram")
plt.show()
