import json 

d = {
    "PONumber": 2608,
    "ShippingInstructions": {
        "name": "John Silver",
        "Address": {
            "street": "426 Light Street",
            "city": "South San Francisco",
            "state": "CA",
            "zipCode": 99237,
            "country": "USA",
        },
        "Phone": [
            {"type": "Office", "number": "809-123-9309"},
            {"type": "Mobile", "number": "417-123-4567"},
        ],
    },
}

# with open("topico10/out.json", "w") as outfile:
#     json.dump(d, outfile)
    
with open("topico10/out.json", "r") as fp:
    e = json.load(fp)
    print(e)