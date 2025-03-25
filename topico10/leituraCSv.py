import csv

path = "topico10/data.csv"

with open(path, "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    
    cars = []
    
    for row in csv_reader:
        cars.append(row)
    
    print(cars)
    