import csv
totalrow_list=[]
with open('dataset/main_dataset.csv', newline='') as csvfile:
    data = csv.DictReader(csvfile)
    print("ID Department Name")
    print("---------------------------------")
    i=0
    flag = 0
    for row in data:
        full_row = row['name'],row['category'],row['img_paths']
        print(full_row)
        totalrow_list.append(full_row)
        
with open('ObjDetTrain.csv', 'w', newline='\n') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(["fileName", "Category", "Paths","Class"])
    csv_writer.writerows(totalrow_list)
