import csv

file = 'Day6_data.txt'
with open(file) as ans:
    groupAns = ans.read().replace('\r\n', '\n').replace('\n\n', '|').replace('\n', ' ').split('|')

sum = 0
for i in groupAns:
    setList = []
    splitted = i.split(' ')
    for j in splitted:
        j = set((j))
        setList.append(j)
    sum += len(setList[0].intersection(*setList))
    print(setList[0].intersection(*setList))
    print('--------')

print(sum)
