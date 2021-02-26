#!/bin/python

# Import the libraries we are using. It is good practice to import all necessary
# libraries in the first lines of a file.

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#test comment
# Create an array (a multi-dimensional table) out of our data file, full of text
all_data = np.genfromtxt("1302_susc_data.csv", delimiter=',',skip_header=3)
print(all_data)

#to divide the data sets in output
print("~~~~~~~~~~~~~~~~~~~~~")
# Select the data range we are interested in, convert it into a new array, full of numbers
susc_data = np.array(all_data[:,:], dtype=float)
print(susc_data)

#Create a figure of the processed data
susc_figure = plt.figure()
susc_plot = plt.scatter (susc_data[:,0],susc_data[:,1])
plt.title ("IODP Expedition 303, Site U1302-03")
plt.xlabel ("Meters Composite Depth")
plt.ylabel ("Magnetic Susceptibility") 
plt.show(block=True)
susc_figure.savefig('./susceptibility-with-depth.png')

#let script write pandas dataset into .json file
all_data = pd.read_csv("1302_susc_data.csv", header=2)
all_data.info()
all_data.to_json("data_output.json")

print(all_data.loc['0.3':'1',:])

json_data = pd.read_json("data_output.json")
json_data.info()

print(json_data.loc['0.3':'1',:])

