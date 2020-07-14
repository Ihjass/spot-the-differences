import get_files as GetFiles
import csv
# get all file names under the given path
allFileNames = GetFiles.getListofFiles('D:\\Nivedhithaa\\Sixth-Semester\\mlpackage\\dataset\\')
row_list = []
# for each file name, accordingly create a row to be added in CSV
for i in range(len(allFileNames)):
    print(allFileNames[i])
    total = [allFileNames[i],"image","Swami"]
    row_list.append(total)

# on opening 'train.csv', write the row that is needed
with open('train.csv','w',newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(["fileName","Size","Type"])
    # for multiple rows use 'writerows' instead of 'writerow'
    csv_writer.writerows(row_list)
