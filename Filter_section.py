# filter_section.py

import numpy as np
from scipy.signal import butter, lfilter
import matplotlib.pyplot as plt

# --- Generate Example Signal ---
fs = 1000  # Sampling frequency (Hz)
t = np.linspace(0, 1, fs, endpoint=False)
signal = np.sin(2 * np.pi * 50 * t) + 0.5 * np.sin(2 * np.pi * 200 * t)

# --- Low-Pass Filter Design ---
def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    return butter(order, normal_cutoff, btype='low', analog=False)

def apply_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order)
    return lfilter(b, a, data)

# --- Apply Filter ---
cutoff = 100  # Hz
filtered_signal = apply_filter(signal, cutoff, fs)

# --- Plot Time-Domain Signals ---
plt.figure(figsize=(8, 4))
plt.plot(t, signal, label='Original Signal')
plt.plot(t, filtered_signal, label='Filtered Signal', linestyle='--')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.title('Signal Before and After Filtering')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
