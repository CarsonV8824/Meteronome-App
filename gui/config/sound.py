import numpy as np
import wave
import struct

# Click settings
sample_rate = 44100
duration = 0.03          # 30 ms
frequency = 2000         # Hz

# Time array
t = np.linspace(0, duration, int(sample_rate * duration), False)

# Sine burst with exponential decay
click = np.sin(2 * np.pi * frequency * t) * np.exp(-t * 50)

# Normalize to 16‑bit range
click = click * 32767 / np.max(np.abs(click))
click = click.astype(np.int16)

# Write to WAV file
with wave.open("metronome_click.wav", "w") as f:
    f.setnchannels(1)          # mono
    f.setsampwidth(2)          # 16‑bit
    f.setframerate(sample_rate)
    f.writeframes(click.tobytes())

print("metronome_click.wav created!")
