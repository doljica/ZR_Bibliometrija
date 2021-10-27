import csv

csv_file = open('data_1-1000.csv')
csv_reader = csv.reader(csv_file)
csv_data = list(csv_reader)

for row in csv_reader:
    print('Row #' + str(csv_reader.line_num) + '' + str(row))
