## Data Preprocessing - Conversion from SEG-Y to NumPy Arrays

This repository contains scripts to preprocess SEG-Y files and convert them to NumPy arrays. 
This is a common preprocessing step in seismic data analysis.

### Installation
To run the scripts in this repository, you need to have the following installed:

```bash
Python 3
NumPy
segyio
automan
```
To install these, you can use pip. For example, to install `automan`, run the following command:

```bash
pip3 install numpy
```

We have also provided a `requirements.txt` file that contains all the required packages. You can install all the required packages by running the following command:

```bash
pip3 install -r requirements.txt
```

### Usage

#### Single File

To preprocess a single SEG-Y file, run the following command:

```bash
python3 data_to_numpy.py --data <path/to/data.sgy> --output <path/to/output.npy> --silent
```
The arguments are as follows:

- *--data data_file_path*: The path to the SEG-Y file to be converted (required).
- *--output output_file_path*: The path to the output binary file (required).
- *--silent*: Optional flag to suppress logging output.
The script will extract some metadata from the SEG-Y file headers, convert the trace data to a NumPy array, and save the array to a binary file (.npy) at the specified output path.

#### Multiple Files -- Automate using Automan

To preprocess multiple SEG-Y files, we can use the `automan` package to automate the process.

The automate.py script uses the automan package to convert multiple SEG-Y files to NumPy arrays. The SEG-Y files should be placed in the `data/` directory. The script creates a npy_data directory where the NumPy arrays are saved.

To run the script, use the following command:

```bash
python3 automate.py
```

The script automatically finds all SEG-Y files in the `data/` directory, convert and save to `.npz` file
 using the `data_to_numpy.py` script.

### Logging

The scripts in this repository use the `logging` module to log messages.