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

    layout = [[sg.Canvas(key='-CANVAS-')],
            [sg.Button('Slider Goes Here')]]

    # create the form and show it without the plot
    window = sg.Window('Matplotlib Popup Window', layout, finalize=True, element_justification='center', font='Helvetica 18')

    # add the plot to the window
    fig_canvas_agg = draw_figure(window['-CANVAS-'].TKCanvas, fig)

    event, values = window.read()
    window.close()

mpl_window(fig)



sg.theme("LightBlue")
#define layout
layout=[
        [sg.Text("Enter start value",font='Lucida'),
         sg.Input(key='stVal',size=(3, 1)),
         sg.Text("Enter end value", font='Lucida'),
         sg.Input(key='enVal',size=(3, 1))],
        [sg.Text("Color map", font ='Lucinda'), sg.Slider(orientation ='horizontal', key='stSlider', range=(1,100))],
        [sg.Text("Variation ", font ='Lucinda'), sg.Slider(orientation ='horizontal', key='endSlider',range=(1,100))],
        [sg.Submit(key='btnSubmit'), sg.Cancel()]
        ]



#Define Window
window =sg.Window("Color Chooser",layout)
#Read  values entered by user
event,values=window.read()

window['stVal'].update(int(values['stSlider']))
window['enVal'].update(int(values['endSlider']))
event,values=window.read()
i=int(values['stVal'])
k=int(values['enVal'])
window['btnSubmit'].set_focus()
val=0

for i in range(k):
    event, values = window.read(timeout=100)
    # update progress bar value
    val=val+100/(k-i)    

window.close()
