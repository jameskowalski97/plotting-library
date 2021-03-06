#!/bin/python
#TODO: fix pylint warnings#
#Rene, I was fixed some pylint warnings, saved the file, and then got a test discovery fail error. The tests were working fine before this save.#


# Import the libraries we are using. It is good practice to import all necessary
# libraries in the first lines of a file.
import os as os
import sys 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Create read_data function
def read_data(filename,delimiter=','):
    """ This function reads data from specified filename. The specified filename
    should point to a specified .csv """
    # Create an array (a multi-dimensional table) out of our data file, full of text
    all_data = np.genfromtxt(filename, delimiter=delimiter,skip_header=3)
    print(all_data)

    # Select the data range we are interested in, convert it into a new array, full of numbers
    susc_data = np.array(all_data[:,:], dtype=float)
    return susc_data

#Create plot_figure function
def plot_figure (susc_data, plot_filename):
    """Create a figure of the processed data"""
    susc_figure = plt.figure()
    susc_plot = plt.scatter (susc_data[:,0],susc_data[:,1])
    plt.title ("IODP Expedition 303, Site U1302-03")
    plt.xlabel ("Meters Composite Depth")
    plt.ylabel ("Magnetic Susceptibility")
    plt.show(block=True)
    susc_figure.savefig(plot_filename)


#Create pandas_to_json function
def pandas_to_json (filename, output_filename):
    """let script write pandas dataset into .json file"""
    all_data = pd.read_csv(filename, header=2)
    all_data.info()
    all_data.to_json(output_filename)

def plot():
    """ plot """
    input_file = "1302_susc_data.csv"
    plot_file = "susceptibility-with-depth.pdf"
    json_output_file = "data_output.json"

    data_directory = os.path.realpath(os.path.join(os.path.dirname(__file__),"..","data"))
    results_directory = os.path.realpath(os.path.join(os.path.dirname(__file__),"..","results"))

    input_filename = os.path.join(data_directory, input_file)
    plot_filename = os.path.join(data_directory, plot_file)
    json_output_file = os.path.join(data_directory, json_output_file)

    susc_data = read_data(input_filename)
    plot_figure(susc_data, plot_filename)
    pandas_to_json(input_filename, json_output_file)

if __name__ == "__main__":
    print(sys.argv)
    plot()
