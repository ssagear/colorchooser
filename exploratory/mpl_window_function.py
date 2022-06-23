#!/usr/bin/env pytho
from jinja2 import ModuleLoader
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import PySimpleGUI as sg
import matplotlib
matplotlib.use('TkAgg')

# ------------------------------- PASTE YOUR MATPLOTLIB CODE HERE -------------------------------
#
# # Goal is to have your plot contained in the variable  "fig"

fig = matplotlib.figure.Figure(figsize=(5, 4), dpi=100)
t = np.arange(0, 3, .01)
fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

# ------------------------------- END OF YOUR MATPLOTLIB CODE -------------------------------

# ------------------------------- Beginning of Matplotlib helper code -----------------------

def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

# ------------------------------- Beginning of GUI CODE -------------------------------

def mpl_window(fig):
    """This function plot a matplotlib figure object in a new window with a slider to choose the fontsize. 
    It returns the slider output."""
    sg.theme("LightBlue")

    """Changed Layout"""
    layout =[[sg.Canvas(key='-CANVAS-')],
            [sg.Text("Color", font ='Lucinda')],
            [sg.In(key='color')],
            [sg.ColorChooserButton(button_text='Choose Color', target='color')],
            [sg.Submit(key='btnSubmit'), sg.Cancel()]
            ]

    # create the form and show it without the plot
    window = sg.Window('Matplotlib Popup Window', layout, finalize=True, element_justification='center', font='Helvetica 18')

    # add the plot to the window
    fig_canvas_agg = draw_figure(window['-CANVAS-'].TKCanvas, fig)
    event, values = window.read()
    window.close()

    """Hex code is contained in values['color']"""
    return values['color']

hex = mpl_window(fig)

"""This part of the code creates a new plot window with the specified fontsize."""
fig = matplotlib.figure.Figure(figsize=(5, 4), dpi=100)
t = np.arange(0, 3, .01)
fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t), color=hex)

mpl_window(fig)