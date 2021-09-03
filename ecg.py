import matplotlib.pyplot as plt
import numpy as np
AUTO = -1

import ecg_example
import pathlib


def render_png(ecg, file_path):
    ecg_arr = np.array(ecg)
    abs_max_ecg = abs(ecg_arr).max()
    ecg_arr = np.array_split(np.trim_zeros(ecg_arr), 5)
    fig, axes = plt.subplots(len(ecg_arr), 1,
                             gridspec_kw={'hspace': 0.1},
                             figsize=(16.6, 23.4))
    for i, (ax, ecg_row) in enumerate(zip(axes, ecg_arr)):
        plt.setp(ax.spines.values(), color='none')
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        ax.xaxis.set_ticks_position('none')
        ax.yaxis.set_ticks_position('none')
        a, b = i * len(ecg_row), (i + 1) * len(ecg_row)
        ax.set_ylim(-abs_max_ecg, abs_max_ecg)
        ax.set_xlim(a, b)
        ax.grid(which='both', linewidth='0.5', color=(1, 0.7, 0.7))
        ax.minorticks_on()
        ax.plot(np.arange(a, b), ecg_row)
    fig.savefig(file_path)


def _test_render_png():
    # Arrange
    ecg = ecg_example.ecg
    title = 'Пациент: ECG Creator Medsenger Agent'
    file_path = 'files/example.png'
    png_path = pathlib.Path(file_path)
    png_path.unlink(missing_ok=True)

    # Act
    render_png(ecg, file_path)

    # Assert
    assert png_path.exists()


if __name__ == '__main__':
    _test_render_png()
