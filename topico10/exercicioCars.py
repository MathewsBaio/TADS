import json

with open("topico10/cars.json") as fp:
    data = json.load(fp)   
    
    for car in data["cars"]:
        for key,value in car.items():
            print(f"{key}: ", value)