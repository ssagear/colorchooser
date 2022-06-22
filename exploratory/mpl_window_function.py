#!/usr/bin/env pytho
from jinja2 import ModuleLoader
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import PySimpleGUI as sg
import matplotlib
matplotlib.use('TkAgg')

"""Streamlined version of https://github.com/PySimpleGUI/PySimpleGUI/blob/master/DemoPrograms/Demo_Matplotlib.py"""


"""
Demonstrates one way of embedding Matplotlib figures into a PySimpleGUI window.
Basic steps are:
 * Create a Canvas Element
 * Layout form
 * Display form (NON BLOCKING)
 * Draw plots onto convas
 * Display form (BLOCKING)
 
 Based on information from: https://matplotlib.org/3.1.0/gallery/user_interfaces/embedding_in_tk_sgskip.html
 (Thank you Em-Bo & dirck)
"""

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
    sg.theme("LightBlue")

    layout =[[sg.Canvas(key='-CANVAS-')],
            [sg.Text("Font Size", font ='Lucinda'), sg.Slider(orientation ='horizontal', key='font', range=(1,100))],
            [sg.Submit(key='btnSubmit'), sg.Cancel()]
            ]

    # create the form and show it without the plot
    window = sg.Window('Matplotlib Popup Window', layout, finalize=True, element_justification='center', font='Helvetica 18')

    # add the plot to the window
    fig_canvas_agg = draw_figure(window['-CANVAS-'].TKCanvas, fig)

    event, values = window.read()
    fontsz = int(values['font'])
    window.close()

    return fontsz

fontsz = mpl_window(fig)


plt.rcParams['font.size'] = fontsz
fig = matplotlib.figure.Figure(figsize=(5, 4), dpi=100)
t = np.arange(0, 3, .01)
fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

mpl_window(fig)