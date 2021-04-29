import csv

items = {
    "Onions": .50,
    "Tomatoes": .99,
    "Eggs": 2.99,
    "Ice Cream": 4.99,
    "Carrots": .75
}

# with open('pricelist.csv', 'w') as f:
#     for key in items.keys():
#         f.write("%s,%s\n" % (key, items[key]))


# mydict = {}

with open('pricelist.csv', mode='r') as inp:
    reader = csv.reader(inp)
    dict_from_csv = {rows[0]: rows[1] for rows in reader}
