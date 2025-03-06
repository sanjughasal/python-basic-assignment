"""Write a Python script which reads a csv file and Visualizes a table with proper indentations and borders. 
(make sure to don’t use any table making module or package)	
Example : CSV file like this
Name,Age,Department
Alice,30,HR
Bob,25,Engineering
Charlie,35,Marketing
Diana,28,Sales"""

import csv

def read_csv(file_path):
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        data = [row for row in csv_reader]
    return data

def print_table(data):
    # Calculate the maximum width of each column
    col_widths = [max(len(str(item)) for item in col) for col in zip(*data)]
    
    # Print the table with borders
    for row in data:
        row_str = " | ".join(f"{item:<{col_widths[i]}}" for i, item in enumerate(row))
        print(f"| {row_str} |")
        if row == data[0]:  # Print the header separator
            print("|" + "|".join("-" * (col_width + 2) for col_width in col_widths) + "|")

if __name__ == "__main__":
    file_path = '/home/sanju/Documents/PythonAssignment/file.csv'  # Replace with your CSV file path
    data = read_csv(file_path)
    print_table(data)