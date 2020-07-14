import numpy as np
import os
import skimage.io as io
import skimage.transform as transform
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
# %matplotlib inline
I = io.imread('dataset/book-covers/Art-Photography/0000002.jpg')/255.0

# making the foreground synthetic
front = I.copy()
front[front>=0.7]=0
plt.axis('off')
plt.imshow(front)
plt.show()
