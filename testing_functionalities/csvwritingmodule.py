import csv
with open('../train.csv','w',newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(["SN","Name","Contributor"])
    csv_writer.writerow(["Windows","Swami","Swami"])