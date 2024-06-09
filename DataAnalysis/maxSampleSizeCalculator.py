# Name:maxSampleSizeCalculator.py
# By: Hayhay
# Purpose: to calculate the maximum sample size in the dataset, so we can interpolate or something to make our neural network batches that size? i'm not quite sure. 

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

sampleSizes = []

for i, item in enumerate(mouseData):
    sampleSize = len(item['raw_path'])
    sampleSizes.append(sampleSize)

sampleSizes = np.array(sampleSizes)
print(f'Maximum Sample Size: {np.max(sampleSizes)}')
print(f'Average Sample Size: {np.mean(sampleSizes)}')
print(f'Mediam Sample Size: {np.median(sampleSizes)}')
print(np.sort(sampleSizes))
