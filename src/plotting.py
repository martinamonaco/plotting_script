#!/bin/python
'''New module'''

import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
'''help(module_name)'''

### Let's refactor the code by adding functions ###

### Import file and copy everything else that was on assignment 2 ###
### Now let's create the first function and generalize "worksheet" into "filename" ###
def read_data(fname, header_lines = 1):
    '''Allows us to automate the reading from file process and convert the data into a np.array'''
    worksheet = pd.read_csv(fname, delimiter='\t',header=header_lines)
    print (worksheet)
    worksheet = np.array(worksheet)

    array_data = np.array(worksheet[1:], dtype=float)
    print(array_data)
    print(array_data.shape)
    #print (type.array_data)
    return array_data

### Added second function ###
def process_data(array_data):
    '''This function will help us trim the original file'''
    relevant_data = array_data[:,1:,]
    #trimmed_data = array_data(#,[1,11],[2,11]])
    #print (trimmed_data,'trimmed data')
    print("Let's remove the column number from the dataset \n", relevant_data)
    print("This is the pyrolite viscosity column \n", relevant_data[:,0])
    return relevant_data

### Make and save figure
### TODO: fix pylint warning (this function takes 2 arguments, so I'm not implementing it) ###
def plot_data(relevant_data,plot_fname):
    '''This function will speed up the plotting process'''
    hefesto_plot = plt.figure()

    #hefesto_scatter = plt.scatter(x = relevant_data[:,0],y=relevant_data[:,1])
    plt.xlabel("Viscosity (Pa s)")
    plt.ylabel("Basalt Percentage in the model box (%)")
    plt.title("Basalt Percentage at the X-Discontinuity — Hefesto values")
    plt.show(block=False)

    hefesto_plot.savefig(plot_fname)

def csv_to_json(fname, output_fname):
    """Convert a csv file named 'fname' to json."""
    all_data = pd.read_csv(fname, header=0, delimiter='\t')
    all_data.info()
    all_data.to_json(output_fname)
### I ultimately want to call this function ###
def plot():
    """Main plotting function."""
    current_file_location = os.path.dirname(__file__)

    data_directory = os.path.join(current_file_location,
                                        "..",
                                        "data")
    results_directory = os.path.join(current_file_location,
                                        "..",
                                        "results")

    input_data_filename = os.path.join(data_directory,
                                        "input.csv")
    array_data = read_data(input_data_filename)
    process_data(array_data)
    relevant_data = process_data(array_data)

    plot_filename = os.path.join(results_directory,
                                        "hefesto.pdf")
    plot_data(relevant_data, plot_filename)

    conversion_filename = os.path.join(data_directory,
                                        "input.csv")
    json_filename = os.path.join(results_directory,
                                        "hefesto_output.json")
    csv_to_json(conversion_filename, json_filename)

 #assert array_data.shape == (50,4), \
  #  "Unexpected size of the array. Array size: " + str(array_data.shape)
plot()
