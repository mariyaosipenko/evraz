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


def renaming(df):

    if (df.name == 7) & (df.podtype_id == 4):
        return 'bearing7_hor'

    if (df.name == 7) & (df.podtype_id == 5):
        return 'bearing7_vert'

    if (df.name == 8) & (df.podtype_id == 4):
        return 'bearing8_hor'

    if (df.name == 8) & (df.podtype_id == 5):
        return 'bearing8_vert'

