plotpainter Tutorial
====================

.. code:: ipython3

    import matplotlib.pyplot as plt
    import numpy as np
    
    from plotpainter import extracted_figure_class as efc
    from plotpainter import run_gui as run
    import PySimpleGUI as sg
    
    %load_ext autoreload
    %autoreload 2


.. parsed-literal::

    The autoreload extension is already loaded. To reload it, use:
      %reload_ext autoreload


Let’s create a set of test plots to see how ``plotpainter`` works. We’ll
create two subplots, each with three individual seta of data.

The entire figure must be stored as a matplotlib Figure object, ``fig``.

.. code:: ipython3

    fig, ax = plt.subplots(1,2,figsize = (10,5))
    
    ax[0].plot([0,1],[0,1],
            color = 'k',
            linewidth = 2, label = 'Peach')
    
    ax[0].plot([1,0],[0,1],
            color = 'b',
            linewidth = 2, label = 'Mango')
    
    ax[0].bar(x = [0,1,2],
              height = [0.1, 0.35, 0.4],
              width = 0.8, label = 'Papaya')
    
    ax[1].scatter([0,1,2], [0,1,2],
                  color = 'purple',
                  marker = 'o', label = 'Kiwi')
    
    ax[1].bar(x = [0,1,2],
              height = [0.25, 0.5, 0.75],
              width = 0.8, label = 'Apple')
    
    ax[1].errorbar([2,3,4], [0,1,2],
                     yerr = [0.1,0.1,0.1],
                     fmt = 'o',
                     capsize = 2,
                     label = 'Banana')
    
    ax[0].set_xlabel('X', fontsize = 14)
    ax[0].set_ylabel('Y', fontsize = 14)
    ax[1].set_xlabel('X', fontsize = 14)
    ax[1].set_ylabel('Y', fontsize = 14)
    ax[0].grid()
    ax[1].grid()
    
    fig.legend()




.. parsed-literal::

    <matplotlib.legend.Legend at 0x7fe459ab6e30>




.. image:: output_3_1.png


.. code:: ipython3

     extractedfig = efc.ExtractedFigure(fig=fig)

To run the app, do ``run.run_GUI(fig)``, passing in your Figure object.

You can specify the subplot and artist (or dataset) for which you intend
to change the color.

When you’re happy with the plot, you can save the file as a png.

To quit the app, click the Exit button.

.. code:: ipython3

    run.run_GUI(fig)


::


    An exception has occurred, use %tb to see the full traceback.


    SystemExit



.. parsed-literal::

    /Users/ssagear/opt/anaconda3/envs/codeastro/lib/python3.10/site-packages/IPython/core/interactiveshell.py:3406: UserWarning: To exit: use 'exit', 'quit', or Ctrl-D.
      warn("To exit: use 'exit', 'quit', or Ctrl-D.", stacklevel=1)


