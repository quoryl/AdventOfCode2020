import csv

numbers = []
results = 0
with open('Day2_data.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=':')
    for row in csv_reader:
        numbers.append(row)

for x in numbers:
    rule = x[0]
    pwd = x[1]
    count = 0
    for l in pwd:
        if l==rule[-1]:
            count += 1

    for i in rule:
        if i=='-':
            lineIndex = rule.index(i)
        elif i==' ':
            spaceIndex = rule.index (i)

    min = int(rule[:lineIndex])
    max = int(rule[lineIndex + 1 : spaceIndex])

    if count >= min and count <= max:
        results += 1

print(results)
print(len(numbers))
