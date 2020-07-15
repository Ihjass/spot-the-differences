# import all modules needed in torch library for the CNN
import torch.nn.functional as tfunc
import torch as tch
import torch.nn as tnn
from sklearn.metrics import roc_curve
from sklearn.metrics import auc
import torch.nn.init

#import local read&process data module
import read_preprocess_imagedata as rd

# RNN Type - defined as a class - inheriting Module of torch nn library.
class RegionalNeuralNet(tch.nn.Module):
    def __init__(self, transform=None):
        super(RegionalNeuralNet, self).__init__()
        # defining the 5 layers
        self.conv1 = tnn.Conv2d(1,10,5)
        self.pool1 = tnn.MaxPool2d(2,2)
        self.conv2 = tnn.Conv2d(10,20,5)
        self.pool2 = tnn.MaxPool2d(2,2)
        self.conv3 = tnn.Conv2d(10, 20, 5)
        self.pool3 = tnn.MaxPool2d(2, 2)
        self.conv4 = tnn.Conv2d(10, 20, 5)
        self.pool4 = tnn.MaxPool2d(2, 2)
        self.conv5 = tnn.Conv2d(10, 20, 5)
        self.pool5 = tnn.MaxPool2d(2, 2)
        self.fc1 = tnn.Linear(320,50)
        self.fc2 = tnn.Linear(50,10)
        # transform so as to be compatible with the type (instead of tensor)
        self.transform = transform
    """"@override"""
    # feeding forward
    def forward(self, inp):
        hidOP = self.pool1(tfunc.sigmoid((self.conv1(inp))))
        forw_OP= self.pool2(tfunc.sigmoid(self.conv2(hidOP)))
        xin = forw_OP.view(forw_OP.size(0),-1)
        xin = tfunc.sigmoid((self.fc1(xin)))
        xin = tfunc.sigmoid(self.fc2(xin))
        return xin
    # if tensor this function transform it to a list
    def __getitem__(self, idx):
        if torch.is_tensor(idx):
            idx = idx.tolist()
# testing the model - accuracy measures
def testModel(fcrnn_model):
    # accuracy
    with torch.no_grad():
        X_test = images_test.test_data.view(len(images_test), 1, 28, 28).float().to(device)
        Y_test = images_test.test_labels.to(device)
    # ROC AUC curve measures
    prob = fcrnn_model.predict_proba(X_test)
    pred = prob[:,1]
    FPRate, TPRate, thresh = roc_curve(y_test, pred)
    auc_area = auc(FPRate, TPRate)
    return auc_area

if __name__ == '__main__':
    device = 'cpu'
    # define an instance of the Type RCNN model.
    fcrnn_model = RegionalNeuralNet().to(device)
    # define the window to be trained
    training_window_sie=30
    global X_train
    global X_test
    global y_test
    global y_train
    # get read, preprocessed data from the rd module
    (X_train, y_train), (X_test, y_test) = rd.getSplitData()
    images_train = (X_train, y_train)
    images_test = (X_test, y_test)
    # load Data
    train_load = tch.utils.data.DataLoader(dataset=images_train)
    test_load = tch.utils.data.DataLoader(dataset=images_test)

    # train the model
    optimizer = tch.optim.Adam(fcrnn_model.parameters())
    loss_function = tch.nn.CrossEntropyLoss()
    total_steps = len(train_load)
    for epochs in range(training_window_sie):
        meancost = 0
        for X,Y in train_load:
            X = X.to(device)
            # Y = Y.to(device)
            optimizer.zero_grad()
            hypothesis = fcrnn_model(X)
            cost_cal = loss_function(hypothesis,Y)
            cost_cal.backward()
            optimizer.step()
            meancost+=cost_cal/total_steps
        print(epochs+1)
        print(meancost)
    # Testing model and check accuracy
    print(testModel(fcrnn_model))
