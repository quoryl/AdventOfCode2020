import csv

def reduce(input, model, A, B):
    rows = []
    for code in input:
        pattern = model
        for letter in code:
            if letter == A:
                pattern = pattern[ : int(len(pattern)/2)]
            elif letter == B:
                pattern = pattern[int(len(pattern)/2) : ]
        if len(pattern) == 1:
            rows.append(pattern[0])
    return rows

input = []
# processing input
with open('Day5_data.txt') as csv_file:
    for line in csv_file:
      input.append(line.strip('\n'))


rows = [ r for r in range(0, 128)]
seats = [ s for s in range(0, 8)]

r = reduce(input, rows, 'F', 'B')
s = reduce(input, seats, 'L', 'R')

# part 1
# find the highest seatID where seatID = row * 8 + seat

combined  = zip (r, s)
max = 0
seatIDs = []
for location in combined:
    seatID = location[0] * 8 + location[1]
    seatIDs.append(seatID)
    if seatID > max:
        max = seatID

print(max)

# part 2
# find your seatId knowing that it is missing from the list but also knowing that
# that seatID -1 and seatID +1 from your seat exist

seatIDs.sort()
for i in range(0, len(seatIDs)):
    if i+1 < len(seatIDs) and seatIDs[i] + 1 != seatIDs[i+1]:
        print(seatIDs[i] + 1)
