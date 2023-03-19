"""
mayavi installation 
===================
pip3 install mayavi
pip3 install PyQt5
===================
"""
import subprocess
import sys

def py_install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


# main function
if __name__ == "__main__":
    # install mayavi and PyQt5
    py_install('mayavi')
    py_install('PyQt5')