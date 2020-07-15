#for reading csv file
import pandas as pd
#pyplot is needed for plotting data
import matplotlib.pyplot as plt
#splitting train and test data 
from sklearn.model_selection import train_test_split

#module to split the data and return tuples of train and test data
def getSplitData():
    train = pd.read_csv('ObjDetTrain.csv')
    test = pd.read_csv('ObjDetTrain.csv')
    train.head()
    X = train.iloc[:, :-1].values
    Y = test.iloc[:, :-1].values
    x_train, x_test, y_train, y_test = train_test_split(X,Y,test_size=0.3,random_state=0)
    return ((x_train, y_train), (x_test, y_test))


if __name__ == '__main__':
    folder = "dataset/"
    nRowsRead = 1000
    df1 = pd.read_csv('ObjDetTrain.csv', delimiter=',', nrows=nRowsRead)
    df1.dataframeName = 'ObjDetTrain.csv'
    num_rows, num_columns = df1.shape
    df1.head(5)
    print(getSplitData())
    print('data split!')
