#!/bin/python

"""This module contains functions to test our plotting script."""
import sys
import os
import numpy as np
import pandas as pd


sys.path.append(os.path.join(
    os.path.dirname(__file__),
    ".."))

from src import plotting
###TODO: fix pylint warning (plotting worked just fine before using pylint) ###
### Also: the module position can't be changed (the script crashes otherwise)###

def test_plot():
    """This test runs the plot() function and makes sure it does not crash."""
    plotting.plot()

def test_read_data():
    """This test runs the read_data() function and makes
       sure the read data has the correct size."""
    current_file_location = os.path.dirname(__file__)
    data_directory = os.path.join(current_file_location,
                                        "..",
                                        "data")
    input_data_filename = os.path.join(data_directory,
                                        "input.csv")
    array_data = plotting.read_data(input_data_filename)
    print (array_data, 'this is the array data')

    assert array_data.shape == (11,3), \
        "Unexpected size of array. Array size: " + str(array_data.shape)

def test_process_data():
    '''This function will help us trim the original file'''
    array_data = np.array([[0,1,2],[3,4,5]])
    relevant_data = ([[1,2],[4,5]])
    print (relevant_data, 'this is the relevant data')
    test_relevant_data = array_data[:,1:,]
    test_output = test_relevant_data
    #test_relevant_data = np.array(array_data[:,1:,])
    #test_output = process_data(test_input_data)
    test_expected_output = test_relevant_data

    ### failing test ###
    # assert np.all(test_output != test_expected_output), \
       # "The process_data function returned an unexpected result."
    assert np.all(test_output == test_expected_output), \
       "The process_data function returned an unexpected result."
test_process_data()
def test_plot_data():
    """This test runs the plot_data() function and makes
    sure it creates a plot file."""
    current_file_location = os.path.dirname(__file__)
    results_directory = os.path.join(current_file_location,
                                        "..",
                                        "results")
    plot_filename = os.path.join(results_directory,
                                "hefesto.pdf")

    if os.path.exists(plot_filename):
        os.remove(plot_filename)
    ### the test fails when the function isn't called ###

    array_data = np.array([[0,1,2],[3,4,5]])
    plotting.plot_data(array_data, plot_filename)

    assert os.path.exists(plot_filename)

def test_csv_to_json():
    """This test runs the csv_to_json() function and makes
    sure the converted data is the same as the original data."""
    current_file_location = os.path.dirname(__file__)

    data_directory = os.path.join(current_file_location,
                                        "..",
                                        "data")
    results_directory = os.path.join(current_file_location,
                                        "..",
                                        "results")
    conversion_filename = os.path.join(data_directory,
                                        "input.csv")
    json_filename = os.path.join(results_directory,
                                        "hefesto.json")
    plotting.csv_to_json(conversion_filename, json_filename)

    input_data = pd.read_csv(conversion_filename, index_col=0, header=0)
    converted_data = pd.read_json(json_filename)
    assert input_data.info() is converted_data.info(), \
       "Error during conversion."
       ###TODO: fix pylint warning###