# README

## Lab Overview

This lab focuses on building a simple in-memory database system in Python. It demonstrates how to load CSV data, store tables in a custom database class, filter table rows, perform aggregations, and join tables together. The objective is to practice object-oriented programming, functional-style data querying, and working with real data from CSV files.

## Project Structure

* **DataLoader**: Handles reading CSV files and converting them into lists of dictionaries.
* **DB**: A lightweight in-memory database that stores and retrieves tables.
* **Table**: Represents a table of data and provides key operations such as filtering, aggregation, and joining.
* **Main Script**: Loads data, inserts tables into the database, performs queries, and prints results.

## Design Overview

### Class: DataLoader

**Attributes:**

* `base_path`: Directory where CSV files are located.

**Key Methods:**

* `load_csv(filename)`: Loads a CSV file and returns a list of dictionaries.

### Class: DB

**Attributes:**

* `tables`: A dictionary storing table names mapped to their data.

**Key Methods:**

* `insert(table)`: Adds a table to the database.
* `search(key_word)`: Retrieves a table by name and returns it as a `Table` object.

### Class: Table

**Attributes:**

* `table_name`: Name of the table.
* `table`: The actual list of row dictionaries.

**Key Methods:**

* `filter(condition)`: Returns a new table with rows satisfying the given condition.
* `aggregate(aggregation_function, aggregation_key)`: Applies an aggregation function to a selected column.
* `join(other_table, key)`: Joins two tables on a shared key and returns a new table.
* `__str__()`: Returns a readable representation of the table.

## How to Test and Run Your Code

1. Ensure the files `Cities.csv` and `Countries.csv` are in the same folder as your script.
2. Run the Python script:

   ```bash
   python main.py
   ```
3. Expected operations that will run:

   * List all cities in Italy
   * Compute average temperature for cities in Italy
   * List all non-EU countries
   * Count countries with coastlines
   * Join the cities and countries tables
   * Filter cities based on temperature and EU membership
   * Find min and max temperatures for EU countries without coastlines

### Additional Testing Scenarios

* Filtering and getting an empty result set
* Aggregating fields with incorrect data formats
* Joining tables with missing or mismatched keys
* Validating handling of non-existent tables in the database
