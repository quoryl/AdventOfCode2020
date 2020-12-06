import csv

file = 'Day6_data.txt'
with open(file) as ans:
    groupAns = ans.read().replace('\r\n', '\n').replace('\n\n', '|').replace('\n', '').split('|')

groupLength = []
for group in groupAns:
    s = set((group))
    groupLength.append(len(s))

print(sum(groupLength))
