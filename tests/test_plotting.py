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
