import csv

numbers = []
results = []
with open('Day1_data.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\n')
    for row in csv_reader:
        toAdd = int(row[0])
        numbers.append(toAdd)

for i in numbers:
    for j in numbers:
        for k in numbers:
            if(i+j+k == 2020):
                results.append(i)
                results.append(j)
                results.append(k)

print(results[0]*results[1]*results[2])
