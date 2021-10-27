import csv

csv_file = open('data_1-1000.csv')
csv_reader = csv.reader(csv_file)
csv_data = list(csv_reader)
print(csv_data[3][2])
