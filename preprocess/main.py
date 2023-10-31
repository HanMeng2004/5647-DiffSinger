# This is a sample Python script.
import librosa
import os
from pyin import wave_to_midi
from pypinyin import pinyin, lazy_pinyin

if __name__ == '__main__':
    # seperate
    os.system('spleeter separate \
      -o audio_output \
      houlai.wav \
      -f {foldername}/{filename}_{instrument}.{codec}')

    # wav->midi
    # print("Starting...")
    # file_in = "audio_output/preprocess/houlai_vocals.wav"
    # file_out = "houlai.mid"
    # y, sr = librosa.load(file_in, sr=None)
    # if not os.path.isfile(file_in):
    #     raise FileNotFoundError(f"The file {file_in} does not exist.")
    # print("Audio file loaded!")
    # midi = wave_to_midi(y, srate=sr)
    # print("Conversion finished!")
    # with open(file_out, 'wb') as f:
    #     midi.writeFile(f)
    # print("Done")
    os.system('basic-pitch /home/hanmeng/DiffSinger/preprocess audio_output/preprocess/houlai_vocals.wav')

    # lyrics->phoneme seq
    with open('lyrics.txt', 'r', encoding='utf-8') as file:
        text = file.read()

    pinyin_with_tone = pinyin(text, style=0)  # 或者 style=1, style=2

    pinyin_without_tone = lazy_pinyin(text)

    with open('output_phoneme.txt', 'w', encoding='utf-8') as file:
        for phoneme in pinyin_with_tone:
            file.write(' '.join(phoneme) + '\n')

    # midi->ds

    # connect to diffsinger
    os.system('python /home/hanmeng/DiffSinger/scripts/infer.py acoustic samples/houlai.ds --exp test_multi --spk '
              'opencpop --out output/houlai')