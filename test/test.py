import numpy as np
import matplotlib.pyplot as plt
import plotpainter as pp

def test_select_subplot():

    from plotpainter import extracted_figure_class as efc
    from plotpainter import run_gui as run

    # Create a test figure with multiple subplots
    fig1, ax1 = plt.subplots(1,2,figsize = (10,5))

    #Subplot 0, Artist 0
    ax1[0].plot([0,1],[0,1],
            color = 'k',
            linewidth = 2)

    #Subplot 0, Artist 1
    ax1[0].plot([1,0],[0,1],
            color = 'b',
            linewidth = 2)
    
    #Subplot 0, Artist 2
    ax1[0].hist(np.random.uniform(0,1,15),
            bins = 10, density = True)

    #Subplot 1, Artist 0
    ax1[1].scatter([0,1,2], [0,1,2],
                color = 'purple',
                marker = 'o')

    #Subplot 1, Artist 1
    ax1[1].bar(x = [0,1,2],
            height = [0.25, 0.5, 0.75],
            width = 0.8)

    #Subplot 1, Artist 2
    ax1[1].errorbar([2,3,4], [0,1,2],
                    yerr = [0.1,0.1,0.1],
                    fmt = 'o',
                    capsize = 2,
                    label = 'silly')

    extractedfig = efc.ExtractedFigure(fig = fig1)

    # Select Subplot 1, Artist 2
    run.run_GUI(fig1)

    return
