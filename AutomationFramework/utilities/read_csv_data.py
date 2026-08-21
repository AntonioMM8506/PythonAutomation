import csv

def get_csv_data(file_name):
    data = []
    with open(file_name, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header row
        for row in reader:
            data.append(tuple(row))
    return data