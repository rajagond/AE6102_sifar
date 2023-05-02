from mayavi import mlab
import numpy as np

data = np.load('data/test1_seismic.npy')

mlab.contour3d(data)
mlab.axes(xlabel='inline', ylabel='crossline', zlabel='depth', nb_labels=5)
mlab.outline()
mlab.show()