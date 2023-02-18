import numpy as np


def get_amplitude(y):
    """
    расчет амплитуды

    """
    np_fft = np.fft.fft(y)
    n_samples = len(np_fft)
    amplitudes = 2 / n_samples * np.abs(np_fft)
    return max(amplitudes)


def check_df_size(df):
    return 0 if len(df) < 5 else 1

