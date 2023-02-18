import numpy as np


def get_amplitude(y):
    """
    расчет амплитуды

    """
    np_fft = np.fft.fft(y)
    n_samples = len(np_fft)
    amplitudes = 2 / n_samples * np.abs(np_fft)
    return max(amplitudes)
