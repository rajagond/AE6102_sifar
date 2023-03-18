"""
mayavi installation 
===================
pip3 install mayavi
pip3 install PyQt5
===================
"""
# import mlab from mayavi
from mayavi import mlab 
# import numpy -- data processing and manipulation
import numpy as np
import subprocess
import sys

def py_install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


# main function
if __name__ == "__main__":
    # install mayavi and PyQt5
    py_install('mayavi')
    py_install('PyQt5')