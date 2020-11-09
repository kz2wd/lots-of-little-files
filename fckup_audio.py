import librosa
import soundfile as sf

path_in = "H:\\bd\\project beat saber folders\\Grind and Hustle - Droeloe.egg"
path_out = "bordel.wav"

sr = 5000

audio, _ = librosa.load(path_in, sr)
print("audio import finish")
sf.write(path_out, audio, sr, sf.default_subtype('WAV'))
print("process done")




