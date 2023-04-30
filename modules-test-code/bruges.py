import numpy as np
import bruges as bg
import matplotlib.pyplot as plt

data = np.load('../data/test1_seismic.npy')

phase = bg.attribute.instantaneous_phase(data.data)

plt.figure(figsize=(6, 10))
plt.imshow(phase[5].T, cmap='twilight_shifted', interpolation='none')
plt.show()