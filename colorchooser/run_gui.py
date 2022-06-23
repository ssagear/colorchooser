import numpy as np
import matplotlib
import matplotlib.pyplot as plt 

def run_GUI(extfig):
    """Runs GUI
    
    Parameters
    __________
    extfig: ExtractedFigureObject

    Returns
    _______
    None
    """

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
    [sg.T('Choose line:  '), sg.Slider(orientation ='horizontal', key='lineSlider', range=(0,3))]
]

    window = sg.Window('Graph with controls', layout)

    while True:
        event, values = window.read()

        hex_code = values['color']

        line_index_float = values['lineSlider']
        line_index = int(line_index_float)

        print(event, values)
        

        if event in (sg.WIN_CLOSED, 'Exit'):  # always,  always give a way out!
            break

        elif event is 'Plot':
            # ------------------------------- PASTE YOUR MATPLOTLIB CODE HERE
            plt.figure(1)
            fig = plt.gcf()
            DPI = fig.get_dpi()
            # ------------------------------- you have to play with this size to reduce the movement error when the mouse hovers over the figure, it's close to canvas size
            fig.set_size_inches(404 * 2 / float(DPI), 404 / float(DPI))
            # -------------------------------
            x = np.linspace(0, 2 * np.pi)
            y = np.sin(x)
            plt.clf()
            plt.plot(x, y, color=hex_code, linestyle=line_type[line_index])
            plt.title('y=sin(x)')
            plt.xlabel('X')
            plt.ylabel('Y')
            plt.grid()

            # ------------------------------- Instead of plt.show()
            draw_figure_w_toolbar(window['fig_cv'].TKCanvas, fig, window['controls_cv'].TKCanvas)

    window.close()



class Toolbar(NavigationToolbar2Tk):
    def __init__(self, *args, **kwargs):
        super(Toolbar, self).__init__(*args, **kwargs)


def draw_figure_w_toolbar(canvas, extfig, canvas_toolbar):
    if canvas.children:
        for child in canvas.winfo_children():
            child.destroy()
    if canvas_toolbar.children:
        for child in canvas_toolbar.winfo_children():
            child.destroy()
    figure_canvas_agg = FigureCanvasTkAgg(extfig.extracted_figure, master=canvas)
    figure_canvas_agg.draw()
    toolbar = Toolbar(figure_canvas_agg, canvas_toolbar)
    toolbar.update()
    figure_canvas_agg.get_tk_widget().pack(side='right', fill='both', expand=1)






