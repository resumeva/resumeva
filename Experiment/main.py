import csv
from mmap import PROT_WRITE

with open('weather.csv', 'r') as file:
    data = list(csv.reader(file))

city = input("City: ")

for row in data[1:]:
    if row[0] == city:
        print(row[1])