import csv

numbers = []
results = 0
inter = []
with open('Day2_data.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=':')
    for row in csv_reader:
        numbers.append(row)

for x in numbers:
    rule = x[0]
    pwd = x[1]

    for i in rule:
        if i=='-':
            lineIndex = rule.index(i)
        elif i==' ':
            spaceIndex = rule.index (i)

    firstPos = int(rule[:lineIndex])
    secondPos = int(rule[lineIndex + 1 : spaceIndex])
    if (pwd[firstPos] == rule[-1] and pwd[secondPos] != rule[-1]) or (pwd[firstPos] != rule[-1] and pwd[secondPos] == rule[-1]):
        results += 1
        inter.append("passed")
    else:
        inter.append("not passed")

print(results)
