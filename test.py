import csv
with open("Cities.csv",'r') as f:
    rows = csv.DictReader(f)
    for i in rows:
        i['dog']

