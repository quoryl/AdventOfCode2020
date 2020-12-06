import csv

input = []

def readData(file):
    fromFile = []
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\n')
        for row in csv_reader:
            fromFile.append(str(row[0]))
    return fromFile

def findTrees(input, rightSlope, downSlope):

    nrRows = len(input)
    nextColumn = 0
    count = 0

    for rowIndex in range(0, nrRows, downSlope):
        nextRow = rowIndex + downSlope
        if(nextRow < nrRows):
            nextColumn = (nextColumn + rightSlope) % len(input[0])
            if input[nextRow][nextColumn] == '#':
                count += 1
    return count

input = readData('Day3_data.txt')
count1 = findTrees(input, 1, 1)
count2 = findTrees(input, 3, 1)
count3 = findTrees(input, 5, 1)
count4 = findTrees(input, 7, 1)
count5 = findTrees(input, 1, 2)
print(count1*count2*count3*count4*count5)
