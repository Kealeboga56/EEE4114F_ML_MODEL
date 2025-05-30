# fft_section.py

import numpy as np
from scipy.fft import fft, fftfreq
import matplotlib.pyplot as plt

# --- Generate Example Signal ---
fs = 1000  # Sampling frequency (Hz)
t = np.linspace(0, 1, fs, endpoint=False)
signal = np.sin(2 * np.pi * 50 * t) + 0.5 * np.sin(2 * np.pi * 200 * t)

# --- Compute FFT ---
N = len(signal)
fft_vals = fft(signal)
freqs = fftfreq(N, 1/fs)
magnitude = np.abs(fft_vals[:N//2])

# --- Plot FFT ---
plt.figure(figsize=(8, 4))
plt.plot(freqs[:N//2], magnitude)
plt.title("FFT of Signal")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Magnitude")
plt.grid(True)
plt.tight_layout()
plt.show()
