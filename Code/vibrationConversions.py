from importMatlabData import import_vib_data as ivd
import numpy as np
from scipy.signal import find_peaks


def get_peaks(filename):
    vib = ivd(filename)
    vib = vib.to_numpy()
    vib = vib.flatten()
    peaks = find_peaks(vib, prominence=0.1, width=5, height=np.mean(vib))
    return peaks


def get_amplitudes(filename):
    peaks = get_peaks(filename)
    amps = peaks[1]['peak_heights'] - peaks[1]['width_heights']
    return amps


def get_frequencies(filename):
    peaks = get_peaks(filename)
    frequencies = []
    last_peak = 0
    for peak in peaks[0]:
        frequency = 1000 / (peak - last_peak)
        frequencies.append(frequency)
        last_peak = peak
    return frequencies


def output_amp_freq(filename):
    amps = get_amplitudes(filename)
    freqs = get_frequencies(filename)
    return amps, freqs
