import matplotlib.pyplot as plt
import numpy as np
AUTO = -1

import ecg_example
import pathlib


def render_png(ecg, file_path):
    ecg_arr = np.array(ecg)
    ecg_arr = np.array_split(np.trim_zeros(ecg_arr), 5)
    fig, axes = plt.subplots(len(ecg_arr), 1,
                             gridspec_kw={'hspace': 0.1},
                             figsize=(16.6, 23.4))

    time = 12

    for i, (ax, ecg_row) in enumerate(zip(axes, ecg_arr)):
        plt.setp(ax.spines.values(), color='none')
        #ax.set_xticklabels([])
        ax.set_yticklabels([])
        #ax.xaxis.set_ticks_position('none')
        ax.yaxis.set_ticks_position('none')
        ax.set_ylim(-3000, 3000)
        ax.set_xlim(time * i, time * (i + 1))
        ax.grid(which='both', linewidth='0.5', color=(1, 0.7, 0.7))
        ax.minorticks_on()
        ax.plot(np.linspace(time * i, time * (i + 1), len(ecg_row)), ecg_row)
    fig.savefig(file_path, bbox_inches='tight')


def _test_render_png():
    # Arrange
    ecg = ecg_example.ecg
    file_path = 'files/example.png'
    png_path = pathlib.Path(file_path)

    try:
        png_path.unlink()
    except:
        pass

    # Act
    render_png(ecg, file_path)

    # Assert
    assert png_path.exists()


if __name__ == '__main__':
    _test_render_png()
