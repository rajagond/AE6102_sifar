"""
Test Mayavi Basic Visualisation
===================
Modules: mayavi, numpy
===================
"""

import numpy as np
from mayavi import mlab

# Load the data
data = np.load('../data/test.npy')
seismic_data = data

# Set figure details
fig = mlab.figure(figure='seismic', bgcolor=(1, 1, 1), fgcolor=(0, 0, 0), size=(1000, 800))

# CrossLine Slice
mlab.volume_slice(seismic_data, slice_index=0, plane_orientation='x_axes', figure=fig)   

#Inline Slice
mlab.volume_slice(seismic_data, slice_index=0,  plane_orientation='y_axes', figure=fig)   

# Depth Slice
mlab.volume_slice(seismic_data, slice_index=0, plane_orientation='z_axes', figure=fig)  

# Show the figure
mlab.show()
