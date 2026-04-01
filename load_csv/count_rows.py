import csv

path = "load_csv/file.csv"

with open(path,"r", newline='') as file:
    reader=csv.reader(file)

    row_count=0
    for row in reader:
        row_count+=1

    print("total number of rows:",row_count)