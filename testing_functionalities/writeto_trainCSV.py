import get_files as GetFiles
import csv

allFileNames = GetFiles.getListofFiles('D:\\Nivedhithaa\\Sixth-Semester\\mlpackage\\dataset\\')
row_list = []
for i in range(len(allFileNames)):
    print(allFileNames[i])
    total = [allFileNames[i],"image","Swami"]
    row_list.append(total)


with open('train.csv','w',newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(["fileName","Size","Type"])
    csv_writer.writerows(row_list)