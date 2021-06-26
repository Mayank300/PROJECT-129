import csv
import pandas as pd

data_set_1 = []
data_set_2 = []




with open('./csv/bright_stars.csv') as f:
    csv_reader_1 = csv.reader(f)
    for row in csv_reader_1: 
        data_set_1.append(row)

headers_1 = data_set_1[0]
planet_data_1 = data_set_1[1:]


for data_point in planet_data_1:
    data_point[2] = data_point[2].lower()

planet_data_1.sort(key=lambda planet_data_1: planet_data_1[2])

with open('./csv/dwarf_stars.csv', 'a+') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers_1)
    csv_writer.writerows(planet_data_1)



#  for second data set  

with open('./csv/dwarf_stars.csv') as f:
    csv_reader_2 = csv.reader(f)
    for row in csv_reader_2: 
        data_set_2.append(row)


headers_2 = data_set_2[0]
planet_data_2 = data_set_2[1:]


header = headers_1 + headers_2

final_planet_data = []

for index,data_row in enumerate(planet_data_1):
    final_planet_data.append(planet_data_1[index] + planet_data_2[index])


with open('./csv/final_data.csv', 'a+') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(header)
    csv_writer.writerows(final_planet_data)


df = pd.read_csv('./csv/final_data.csv')
df = df[df['Luminosity'].notna()]