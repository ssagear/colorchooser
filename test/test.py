import pytest
import matplotlib.pyplot as plt
import numpy as np
import pdb

from ../extracted_figure_class import ExtractedFigure

def test_successful_artist_extraction():
    """
    Given an ExtractedFigure object created with a matplotlib.figure.Figure object,
    ensure that the artists are all being extracted from the figure.
    """

    # Create plot for ExtractedFigure
    fig, ax = plt.subplots(1, 1, figsize = (5,5))

    ax.bar(x = np.array([1,2,3]),
           height = np.array([0.5,1.0,1.5]),
           width = 0.8,
           color = 'b',
           label = 'Bars')

    ax.plot(np.array([1,2,3]),
            np.array([0.5,1.0,1.5]),
            color = 'k',
            linewidth = 2,
            label = 'Good line')

    ax.errorbar(x = np.array([1,2,3]),
                y = np.array([0.5,1.0,1.5]),
                yerr = np.array([0.1, 0.1, 0.1]),
                color = 'k',
                fmt = 'o',
                capsize = 2)

    ax.set_xlabel('X', fontsize = 14)
    ax.set_ylabel('Y', fontsize = 14)

    # Create the ExtractedFigure object
    extractedfig = ExtractedFigure(fig = fig)

    return
