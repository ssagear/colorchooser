from re import sub
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from plotpainter import extracted_figure_class as efc
import PySimpleGUI as sg

def run_GUI(fig):
    """Runs GUI

    Parameters
    __________
    extfig: ExtractedFigureObject

    Returns
    _______
    None
    """

    extractedfig = efc.ExtractedFigure(fig=fig)
    
    subplots = []
    subplots_ints = []
    artists = []
    artists_ints = []

    for i in range(len(extractedfig.extracted_artist_list)):
        subplots.append('Subplot ' + str(i))
        subplots_ints.append(i)
        for j in range(len(extractedfig.extracted_artist_list[i])):
            artists.append('Artist ' + str(j))
            artists_ints.append(j)

    subplots = np.array(subplots)
    artists= np.array(artists)

    print(subplots)

    
    line_type = ['solid', 'dotted', 'dashed', 'dashdot']

    layout = [
    [sg.T('Graph')],
    [sg.B('Plot'), sg.B('Exit')],
    [sg.T('Controls:')],
    [sg.Canvas(key='controls_cv')],
    [sg.T('Figure:')],
    [sg.Column(
        layout=[
            [sg.Canvas(key='fig_cv',
                       # it's important that you set this size
                       size=(400 * 2, 400)
                       )]
        ],
        background_color='#DAE0E6',
        pad=(0, 0)
    )],
    [sg.In(key='color')],
    [sg.ColorChooserButton(button_text='Choose Color', target='color')],
    [sg.Listbox(values=list(subplots), select_mode='extended', key='subplt', size=(30, 6))],
    [sg.Listbox(values=list(artists), select_mode='extended', key='artst', size=(30, 6))],
    [sg.T('Choose line:  '), sg.Slider(orientation ='horizontal', key='lineSlider', range=(0,3))]
]

    window = sg.Window('Graph with controls', layout, finalize=True)
    draw_figure_w_toolbar(window['fig_cv'].TKCanvas, extractedfig.extracted_figure, window['controls_cv'].TKCanvas)

    while True:
        event, values = window.read()

        print(values['subplt'][-1][-1])
        splot = int(values['subplt'][-1][-1])
        art = int(values['artst'][-1][-1])
        hex_code = values['color']

        line_index_float = values['lineSlider']
        line_index = int(line_index_float)

        print(event, values)


        if event in (sg.WIN_CLOSED, 'Exit'): 
            break

        elif event is 'Plot':
            # ------------------------------- PASTE YOUR MATPLOTLIB CODE HERE
            #plt.figure(1)
            #fig = plt.gcf()
            print(splot, art)
            DPI = extractedfig.extracted_figure.get_dpi()
            # ------------------------------- you have to play with this size to reduce the movement error when the mouse hovers over the figure, it's close to canvas size
            extractedfig.extracted_figure.set_size_inches(404 * 2 / float(DPI), 404 / float(DPI))
            extractedfig.extracted_artist_list[splot][art].set_color(hex_code)
            # -------------------------------
            #x = np.linspace(0, 2 * np.pi)
            #y = np.sin(x)
            #plt.clf()
            #plt.plot(x, y, color=hex_code, linestyle=line_type[line_index])

            # ------------------------------- Instead of plt.show()
            draw_figure_w_toolbar(window['fig_cv'].TKCanvas, extractedfig.extracted_figure, window['controls_cv'].TKCanvas)

    window.close()



class Toolbar(NavigationToolbar2Tk):
   def __init__(self, *args, **kwargs):
       super(Toolbar, self).__init__(*args, **kwargs)


def draw_figure_w_toolbar(canvas, fig, canvas_toolbar):
    if canvas.children:
        for child in canvas.winfo_children():
            child.destroy()
    if canvas_toolbar.children:
        for child in canvas_toolbar.winfo_children():
            child.destroy()
    figure_canvas_agg = FigureCanvasTkAgg(fig, master=canvas)
    figure_canvas_agg.draw()
    toolbar = Toolbar(figure_canvas_agg, canvas_toolbar)
    toolbar.update()
    figure_canvas_agg.get_tk_widget().pack(side='right', fill='both', expand=1)
