import json
import csv


with open("data.json","r") as json_file:
    data=json.load(json_file)


keys=data[0].keys()

with open("output.csv","wb") as csv_file:
    writer=csv.DictWriter(csv_file,fieldnames=keys)

    writer.writeheader()
    writer.writerrows(data)

print("JSON data successfully converted to CSV")