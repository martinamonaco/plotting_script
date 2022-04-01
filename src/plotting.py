import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
### Add new modules for assignment ###
import sys 
import os

### Let's refactor the code by adding functions ###

### Import file and copy everything else that was on assignment 2 ###
### Now let's create the first function and generalize "worksheet" into "filename" ###
def read_data(fname, header_lines = 1):
    #fname = '../data/input.csv'
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
    print("Let's remove the column number from the dataset \n", relevant_data)
    print("This is the pyrolite viscosity column \n", relevant_data[:,0])
    return relevant_data

### Make and save figure
def plot_data(relevant_data,plot_fname):
    '''This function will speed up the plotting process'''
    hefesto_plot = plt.figure()

    hefesto_scatter = plt.scatter(x = relevant_data[:,0],y=relevant_data[:,1])
    plt.xlabel("Viscosity (Pa s)")
    plt.ylabel("Basalt Percentage in the model box (%)")
    plt.title("Basalt Percentage at the X-Discontinuity — Hefesto values")
    plt.show(block=False)

    plot_fname = os.path.join("hefesto.pdf")

    hefesto_plot.savefig(plot_fname)
    

fname = './data/input.csv'
#array_data = (fname, header_lines = 0
array_data = read_data(fname, header_lines = 0)
process_data(array_data)
relevant_data = process_data(array_data)
plot_data(relevant_data,'hefesto.pdf')


### Use pd and make .json file
all_data = pd.read_csv("./data/input.csv", index_col = 0, header=0) ### first column needs to be the index. It starts from 0
all_data.info()
all_data.head()
all_data.to_json("hefesto.json")

json_data = pd.read_json("hefesto.json")
json_data.info()

### Added a small modification just to see if the "M" popped up next to the file
### The file looks pretty clean already, so I have no idea what to remove from it!
### I'll stage the changes and then commit them 
