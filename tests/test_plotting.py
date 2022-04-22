#!/bin/python

import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
### Add new modules for assignment ###
import sys 
import os

sys.path.append(os.path.join(
    os.path.dirname(__file__),
    ".."))

from src import plotting

def test_plot():
    plotting.plot()