"""
Data Preprocessing 
"""

import segyio
import numpy as np
import os
from matplotlib import pyplot as plt
import argparse
import logging

def segy_to_numpy(data_path, output_path):
    """
    Convert SEG-Y files to NumPy arrays
    and save them to binary files (.npy)
    """
    # Open the SEG-Y files in the data folder
    if not data_path.endswith('.sgy') and not data_path.endswith('.segy'):
        data_path = data_path + '.sgy'

    logging.info("------------------------------------------")
    logging.info("Processing file: " + data_path)
    # Open the SEG-Y file for reading
    with segyio.open(data_path, 'r', ignore_geometry=True) as segyfile:
        # Extract some metadata from the file headers
        logging.info('Amplitude Inline range: ' + str(np.amin(segyfile.ilines)) + ' - ' +str(np.amax(segyfile.ilines)))
        logging.info('Amplitude Crossline range: ' + str(np.amin(segyfile.xlines)) + ' - ' +str(np.amax(segyfile.xlines)))
        logging.info("------------------------------------------")
        ntraces = segyfile.tracecount
        nsamples = segyfile.samples.size

        # # Initialize a NumPy array to hold the trace data
        # data = np.zeros((ntraces, nsamples))

        # # Loop over all traces in the file
        # for i in range(ntraces):
        #     # Read the trace data and store it in the NumPy array
        #     data[i, :] = segyfile.trace[i]

        data = np.array([segyfile.trace[i] for i in range(ntraces)])

        logging.info("Number of traces: " + str(ntraces) + " Number of samples: " + str(nsamples))

        logging.info("------------------------------------------")

        # View the binary header
        logging.info(segyfile.bin)
        logging.info("------------------------------------------")

        # View the trace header
        logging.info(segyfile.header[0])
        logging.info("------------------------------------------")

        # View the trace data
        logging.info(segyfile.trace[0])
        logging.info(len(segyfile.trace[0]))
        logging.info("------------------------------------------")

        # The NumPy array 'data' now contains the trace data from the SEG-Y file
        # Save the NumPy array to a binary file
        np.savez(output_path, data)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Data Preprocessing - Conversion from SEG-Y to NumPy Array')
    parser.add_argument('--data', type=str, default='../data/test.sgy', help='Path to the data folder')
    parser.add_argument('--output', type=str, default='../data/test.npy', help='Path to the output folder')
    parser.add_argument('--silent', action='store_true', default=False , help='Silently perform the conversion') 
    args = parser.parse_args()
    if not args.silent:
        logging.basicConfig(level=logging.DEBUG)
    
    logging.info("Data Preprocessing - Conversion from SEG-Y to NumPy Array")

    segy_to_numpy(args.data, args.output)

    logging.info("Conversion completed")