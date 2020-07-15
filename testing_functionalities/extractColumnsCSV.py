#csv module is needd here for copying specific colmuns to another csv
import csv
totalrow_list=[]
# copy from train to test - wohtout the class labels
with open('ObjDetTrain.csv', newline='') as csvfile:
    data = csv.DictReader(csvfile)
    print("----------Data----------")
    print("------------------------")
    i=0
    flag = 0
    for row in data:
        i+=1
        actual_result = row['Class']
        if(i<=20):
            continue

        if i>20 and i<150:
            full_row = row['fileName'],row['Category'],row['Paths']
            print(full_row)
            totalrow_list.append(full_row)
        else:
            break
# write into test file 
with open('ObjDetTest.csv', 'w', newline='\n') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(["fileName", "Category", "Paths"])
    csv_writer.writerows(totalrow_list)
