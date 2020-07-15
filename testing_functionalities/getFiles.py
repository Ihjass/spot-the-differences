#import os to locate file on system
# this file is a helper to other files
import os
def getListofFiles(folder):
    listOfFiles = os.listdir(folder)
    allFiles = list()
    for fileentry in listOfFiles:
        allFiles.append(fileentry)
    return allFiles

# print(getListofFiles('D:\\Nivedhithaa\\Sixth-Semester\\mlpackage\\dataset\\train_zip\\train'))
