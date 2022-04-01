import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
### Add new modules for assignment ###
import sys 
import os

### Let's refactor the code by adding functions ###

### Import file and copy everything else that was on assignment 2 ###
### Now let's create the first function and generalize "worksheet" into "filename" ###
def read_data(filename, header_lines = 0):
    '''Allows us to automate the reading from file process and convert the data into a np.array'''
    worksheet = np.genfromtxt(filename, delimiter=',',skip_header=header_lines)
    array_data = np.array(worksheet[1:], dtype=float)
    print(array_data)
    print(array_data.shape)
    print (type.array_data)
    return data


###worksheet = np.genfromtxt("hefesto_fixed_dataset.csv", delimiter=',',skip_header=0)
print (worksheet)
print(type(worksheet))

array_data = np.array(worksheet[1:], dtype=float)
print(array_data)
print(array_data.shape)
print (type.array_data)

### Added second function ###
def process_data():
    '''This function will help us trim the original file'''
    relevant_data = array_data[:,1:,]
    print("Let's remove the column number from the dataset \n", relevant_data)
    print("This is the pyrolite viscosity column \n", relevant_data[:,0])
    return relevant_data

### Make and save figure
hefesto_plot = plt.figure()

hefesto_scatter = plt.scatter(x = relevant_data[:,0],y=relevant_data[:,1])
plt.xlabel("Viscosity (Pa s)")
plt.ylabel("Basalt Percentage in the model box (%)")
plt.title("Basalt Percentage at the X-Discontinuity — Hefesto values")
plt.show(block=True)

hefesto_plot.savefig('./hefesto_test_plot.png')

### Use pd and make .json file
all_data = pd.read_csv("hefesto_fixed_dataset.csv", index_col = 0, header=0) ### first column needs to be the index. It starts from 0
all_data.info()
all_data.head()
all_data.to_json("hefesto.json")

json_data = pd.read_json("hefesto.json")
json_data.info()

### Added a small modification just to see if the "M" popped up next to the file
### The file looks pretty clean already, so I have no idea what to remove from it!
### I'll stage the changes and then commit them 
