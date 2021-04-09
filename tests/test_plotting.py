import sys, os
import numpy as np
import pandas as pd


sys.path.append(os.path.join(
    os.path.dirname(__file__),
    ".."))

import src.plotting as plotting

#This Test function checks if the plotting function works
def test_plot():
    assert(plotting.plot() == None)

#This test function checks if the data is being read correctly from the .csv file
def test_read_data():
    input_file = "1302_susc_data.csv"
    data_directory = os.path.realpath(os.path.join(os.path.dirname(__file__),"..","data"))
    input_filename = os.path.join(data_directory, input_file)
    susc_data = plotting.read_data(input_filename, starting_row=0)

    assert(susc_data[0,1] == 0.2827)


#This test function checks if the data can be plotted
def test_plot_figure():
    plot_file = "test_plot_figure.pdf"
    results_directory = os.path.realpath(os.path.join(os.path.dirname(__file__),"..","results"))
    plot_filename = os.path.join(results_directory,plot_file)

    input_data = np.array([[0,0],[2,101]])

    if os.path.exists(plot_filename):
        os.remove(plot_filename)
        
    plotting.plot_figure(input_data, plot_filename)

    assert (os.path.exists(plot_filename))