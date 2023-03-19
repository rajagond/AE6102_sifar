"""
Data Preprocessing 
===================
Modules: segyio, numpy
===================
"""

import segyio
import numpy as np

# Open the SEG-Y file for reading
with segyio.open('../data/test.sgy', 'r', ignore_geometry=True) as segyfile:
    
    # Extract some metadata from the file headers
    ntraces = segyfile.tracecount
    nsamples = segyfile.samples.size
    
    # Initialize a NumPy array to hold the trace data
    data = np.zeros((ntraces, nsamples))
    
    # Loop over all traces in the file
    for i in range(ntraces):
        # Read the trace data and store it in the NumPy array
        data[i, :] = segyfile.trace[i]

    print("Number of Traces:", ntraces, ",", "Number of Samples:", nsamples)
        
# The NumPy array 'data' now contains the trace data from the SEG-Y file
# Save the NumPy array to a binary file
np.save('../data/test.npy', data)


