"""
Data Preprocessing 
"""

import segyio
import numpy as np
import os
from matplotlib import pyplot as plt

print("Data Preprocessing - Conversion from SEG-Y to NumPy Array")

# Open the SEG-Y files from the data folder
for file in os.listdir('../data'):
    if file.endswith('.sgy'):
        print("------------------------------------------")
        print("Processing file:", file)
        # Open the SEG-Y file for reading
        with segyio.open('../data/'+file, 'r', ignore_geometry=True) as segyfile:
            
            # Extract some metadata from the file headers
            print('Amplitude Inline range: ' + str(np.amin(segyfile.ilines)) + ' - ' +str(np.amax(segyfile.ilines))) 
            print('Amplitude Crossline range: ' + str(np.amin(segyfile.xlines)) + ' - ' +str(np.amax(segyfile.xlines)))
            print("------------------------------------------")
            ntraces = segyfile.tracecount
            nsamples = segyfile.samples.size
            
            # Initialize a NumPy array to hold the trace data
            data = np.zeros((ntraces, nsamples))
            
            # Loop over all traces in the file
            for i in range(ntraces):
                # Read the trace data and store it in the NumPy array
                data[i, :] = segyfile.trace[i]

            print("Number of Traces:", ntraces, ",", "Number of Samples:", nsamples) 
            print("------------------------------------------")

            # View the binary header
            print(segyfile.bin)
            print("------------------------------------------")

            # View the trace header
            print(segyfile.header[0])
            print("------------------------------------------")

            # View the trace data
            print(segyfile.trace[0])
            print(len(segyfile.trace[0]))
            print("------------------------------------------")

        # The NumPy array 'data' now contains the trace data from the SEG-Y file
        # Save the NumPy array to a binary file
        np.save('../data/'+file[:-4]+'.npy', data) 


