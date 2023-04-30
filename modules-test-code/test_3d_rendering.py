from mayavi import mlab
import numpy as np

data = np.load('../data/test1_seismic.npy')

source = mlab.pipeline.scalar_field(data)

mlab.pipeline.volume(source)
mlab.axes(xlabel='inline', ylabel='crossline', zlabel='depth', nb_labels=5)
mlab.outline()
mlab.show()