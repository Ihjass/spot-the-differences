import numpy as np
import os
import skimage.io as io
import skimage.transform as transform
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
# %matplotlib inline

image_path = ''
I = io.imread(image_path)/255.0

# making the foreground synthetic
front = I.copy()
front[front>=0.9]=0
plt.axis('off')
plt.imshow(front)
plt.show()
