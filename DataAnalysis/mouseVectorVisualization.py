# Name: mouseVectorVisualization.py
# By: Hayhay
# Purpose: This script is to help do data analysis on the mouse clicks! I want to use this to help figure out what the vectors look like so we know what we're going to be feeding the neural network!

import json
import matplotlib as mlp
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

filepath = '../deserialized_data.json'

with open(filepath, 'r') as file:
        mouseData = json.load(file)
       
#for i, item in enumerate(mouseData):
#    print(f"keys {i+1}: {list(item.keys())}")
# These are the outputs of the data names
# ['start_timestamp', 'batch_id', 'end_timestamp', 'destination', 'source', 'translation', 'raw_path', 'duration', 'interpolated_path'] 
# start_timestamp has 'int' type
# end_timestamp has 'int' type
# raw_path has 'dict' type

count = 0

sampleSizes = []

for i, item in enumerate(mouseData):
    # Don't go past the first dataset
    if count == 1:
        break
    
    # Setting up to pull values into a list
    x = []
    y = []
    t = []
    
    # Setting up the figure to make a plot later on
    '''fig, ax = plt.subplots()
    ax.set_xlim(-1000, 1000)
    ax.set_ylim(-1000, 1000)
    ax.set_aspect('equal', 'box')
    ax.grid(True)
'''
    # Pulling the duration
    duration = item['duration']
    # print(f'duration: {duration}')

    # Pulling the data point dictionarys with X, Y, and Z 
    mousePointDicts = item['raw_path']
    
    # Putting all coordinate points into lists for easier manipulation
    for value in mousePointDicts:
        x.append(value['x'])
        y.append(value['y'])
        t.append(value['t'])

    x = np.array(x)
    y = np.array(y)
    t = np.array(t)

    # Calculate the deltaX's and deltaY's
    deltaX = x[1:] - x[:-1]
    deltaY = y[1:] - y[:-1]
    deltaT = t[1:] - t[:-1]
    
    sampleSizes.append(len(x))

    #print(deltaX)
    #print(deltaY)
    #print(deltaT)

    # Up the counter of which mouse path we are looking at
    # count = count + 1

print(max(sampleSizes))
