import csv, os
from pathlib import Path

class DataLoader:
    """Handles loading CSV data files."""
    
    def __init__(self, base_path=None):
        """Initialize the DataLoader with a base path for data files.
        """
        if base_path is None:
            self.base_path = Path(__file__).parent.resolve()
        else:
            self.base_path = Path(base_path)
    
    def load_csv(self, filename):
        """Load a CSV file and return its contents as a list of dictionaries.
        """
        filepath = self.base_path / filename
        data = []
        
        with filepath.open() as f:
            rows = csv.DictReader(f)
            for row in rows:
                data.append(dict(row))
        
        return data

class DB:
    """Your code here"""
    def __init__(self):
        self.tables = {}

    def insert(self, table):
        self.tables[table.table_name] = table

    def search(self, table_name):
        return self.tables.get(table_name)
    
class Table:
    """Your code here"""

    def __init__(self, table_name, table):
        self.table_name = table_name
        self.table = table  # list of dictionaries

    def filter(self, func):
        filtered = list(filter(func, self.table))
        return Table(self.table_name + "_filtered", filtered)

    def aggregate(self, func, column):
        values = [float(row[column]) for row in self.table]
        return func(values)

    def join(self, other_table, key):
        joined_table = []
        for row1 in self.table:
            for row2 in other_table.table:
                if row1[key] == row2[key]:
                    combined = {**row1, **row2}
                    joined_table.append(combined)
        return Table(f"{self.table_name}_joined_{other_table.table_name}", joined_table)
    
    def __str__(self):
        return self.table_name + ':' + str(self.table)

loader = DataLoader()
cities = loader.load_csv('Cities.csv')
table1 = Table('cities', cities)
countries = loader.load_csv('Countries.csv')
table2 = Table('countries', countries)

my_DB = DB()
my_DB.insert(table1)
my_DB.insert(table2)

# List all cities in Italy
my_table1 = my_DB.search('cities')
cities_filtered = my_table1.filter(lambda x: x['country'] == 'Italy')
print("List all cities in Italy:")
print(f"cities_filtered:{cities_filtered.table}\n")

# Average temperature for all cities in Italy
print("Average temperature for all cities in Italy:")
print(cities_filtered.aggregate(lambda x: sum(x)/len(x), 'temperature'))
print()

# List all non-EU countries
my_table2 = my_DB.search('countries')
countries_filtered = my_table2.filter(lambda x: x['EU'] == 'no')
print("List all non-EU countries:")
print(f"countries_filtered:{countries_filtered.table}\n")

# Number of countries that have coastline
coastline_count = my_table2.filter(lambda x: x['coastline'] == 'yes').aggregate(lambda x: len(x), 'coastline')
print("Number of countries that have coastline:")
print(coastline_count)
print()

# Join tables
my_table3 = my_table1.join(my_table2, 'country')
print("First 5 entries of the joined table (cities and countries):")
for item in my_table3.table[:5]:
    print(item)
print()

# Cities whose temperatures are below 5.0 in non-EU countries
my_table3_filtered = my_table3.filter(lambda x: x['EU'] == 'no').filter(lambda x: float(x['temperature']) < 5.0)
print("Cities whose temperatures are below 5.0 in non-EU countries:")
print(my_table3_filtered.table)
print()

# Min and max temperatures for cities in EU countries without coastlines
my_table3_filtered = my_table3.filter(lambda x: x['EU'] == 'yes').filter(lambda x: x['coastline'] == 'no')
print("The min and max temperatures for cities in EU countries that do not have coastlines")
print("Min temp:", my_table3_filtered.aggregate(lambda x: min(x), 'temperature'))
print("Max temp:", my_table3_filtered.aggregate(lambda x: max(x), 'temperature'))