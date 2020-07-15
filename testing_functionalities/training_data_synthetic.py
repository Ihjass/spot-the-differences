#import numpy for any conversions to array
import numpy as np
#import os for locating path
import os
#for synthesis - import skimage modules
import skimage.io as io
import skimage.transform as transform
#for visualising data import matplotlib modules
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
# %matplotlib inline
imag_name=''
I = io.imread(imag_name)/255.0

# making the foreground synthetic
front = I.copy()
front[front>=0.7]=0
plt.axis('off')
plt.imshow(front)
plt.show()
