import os
import wave
import midiutil
import sys
import librosa
from sound_to_midi.monophonic import wave_to_midi


def create_midi_from_wav(wav_file_path: str, midi_file_path: str):
    """
    Converts a WAV sound file to a MIDI file.

    Parameters:
    - wav_file_path: str
        The path to the input WAV sound file.
    - midi_file_path: str
        The path to save the output MIDI file.

    Raises:
    - FileNotFoundError:
        If the input WAV file does not exist.
    """

    # Check if the input WAV file exists
    if not os.path.exists(wav_file_path):
        raise FileNotFoundError("Input WAV file does not exist.")

    # Open the WAV file
    with wave.open(wav_file_path, 'rb') as wav_file:
        # Get the audio parameters
        sample_width = wav_file.getsampwidth()
        frame_rate = wav_file.getframerate()
        num_frames = wav_file.getnframes()
        num_channels = wav_file.getnchannels()

        # Read the audio data from the WAV file
        audio_data = wav_file.readframes(num_frames)

    # Create a MIDI file
    midi_file = midiutil.MIDIFile(num_channels)

    # Set the tempo and time signature
    tempo = 120  # Adjust the tempo as needed
    time_signature = (4, 4)  # Adjust the time signature as needed
    midi_file.addTempo(0, 0, tempo)
    midi_file.addTimeSignature(0, 0, *time_signature)

    # Convert the audio data to MIDI events
    for i in range(num_frames):
        # Get the sample value for each channel
        sample_values = []
        for j in range(num_channels):
            sample_start = i * num_channels * sample_width
            sample_end = sample_start + sample_width
            sample_data = audio_data[sample_start:sample_end]
            sample_value = int.from_bytes(sample_data, byteorder='little', signed=True)
            sample_values.append(sample_value)

        # Add the MIDI events for each channel
        for channel, sample_value in enumerate(sample_values):
            # Scale the sample value to the MIDI range (0-127)
            midi_value = int((sample_value / (2 ** (8 * sample_width))) * 127)

            # Add a note event with the MIDI value
            midi_file.addNote(channel, 0, midi_value, i, i + 1, velocity=100)

    # Save the MIDI file
    with open(midi_file_path, 'wb') as midi_file:
        midi_file.writeFile(midi_file_path)


print("Starting...")
file_in = "01_xiaoyaoxian-man1.wav"
file_out = "xiaoyaoxian.mid"
y, sr = librosa.load(file_in, sr=None)
print("Audio file loaded!")
midi = wave_to_midi(y, srate=sr)
print("Conversion finished!")
with open (file_out, 'wb') as f:
    midi.writeFile(f)
print("Done. Exiting!")