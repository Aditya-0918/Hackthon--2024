import sounddevice as sd
import numpy as np
import wave

# Parameters
samplerate = 44100  # Hertz
duration = 10  # seconds

# Record audio
print("Recording...")
recording = sd.rec(int(samplerate * duration), samplerate=samplerate, channels=1, dtype='int16')
sd.wait()  # Wait until recording is finished
print("Recording finished.")

# Save the recording as a WAV file
filename = 'test_sound.wav'
with wave.open(filename, 'wb') as wf:
    wf.setnchannels(1)
    wf.setsampwidth(2)  # 2 bytes (16 bits)
    wf.setframerate(samplerate)
    wf.writeframes(recording.tobytes())

print(f"Audio saved to {filename}")