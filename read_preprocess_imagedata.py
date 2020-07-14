import matplotlib.pyplot as plt
import pandas as pd
import os
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
#
#
# def getSplitData():
#     train = pd.read_csv('ObjDetTrain.csv')
#     train.head()
#     X = train.iloc[:, :-1].values
#     Y = train.iloc[:, -1].values
#     x_train, x_test, y_train, y_test = train_test_split(X,Y,test_size=0.3,random_state=0)
#     return ((x_train, y_train), (x_test, y_test))
#
#
# if __name__ == '__main__':
#     nRowsRead = 1000
#     df1 = pd.read_csv('ObjDetTrain.csv', delimiter=',', nrows=nRowsRead)
#     df1.dataframeName = 'ObjDetTrain.csv'
#     nRow, nCol = df1.shape
#     print(f'There are {nRow} rows and {nCol} columns')
#     df1.head(5)
#     print(getSplitData())

import pandas as pd
import cv2 as cvimg
import numpy as np
import os
import matplotlib.pyplot as plt
import glob

def getSplitData():
    train = pd.read_csv('dataset/ObjDetTrain.csv')
    train.head()
    X = train.iloc[:, :-1].values
    Y = train.iloc[:, -1].values
    x_train, x_test, y_train, y_test = train_test_split(X,Y,test_size=0.3,random_state=0)
    return ((x_train, y_train), (x_test, y_test))

def flatten_images():
    for filename in os.listdir(folder):
        print(filename)
        img=plt.imread(folder+filename)  # reading image (Folder path and image name )
        img=np.array(img)                #
        img=img.flatten()                # Flatten image
        images.append(img)               # Appending all images in 'images' list
    return images


if __name__ == '__main__':
    folder = "dataset/"
    nRowsRead = 1000
    df1 = pd.read_csv('ObjDetTrain.csv', delimiter=',', nrows=nRowsRead)
    df1.dataframeName = 'ObjDetTrain.csv'
    nRow, nCol = df1.shape
    print(f'There are {nRow} rows and {nCol} columns')
    df1.head(5)
    print(getSplitData())
    images=[]                             # list contatining  all images
    print(flatten_images())

