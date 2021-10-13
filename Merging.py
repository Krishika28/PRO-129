import csv

list_1 = []
list_2 = []

with open('bright_stars.csv', 'r') as f:
    data_read = csv.reader(f)
    for i in data_read:
        list_1.append(i)

with open('Clean_dwarf_stars.csv', 'r') as f:
    data_read = csv.reader(f)
    for i in data_read:
        list_2.append(i)

header1 = list_1[0]
header2 = list_2[0]

planet_data1 = list_1[1:]
planet_data2 = list_2[1:]

headers = header1+header2

planet_data = []

for index, row in enumerate(planet_data1):
    planet_data.append(planet_data1[index]+planet_data2[index])

with open('merged_data.csv', 'a+') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(planet_data)