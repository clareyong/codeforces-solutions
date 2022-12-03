import sys
lines = sys.stdin.readlines()
n, m = map(int, lines[0].rstrip().split())
array = list(map(int, lines[1].rstrip().split()))
operations = list()
interested = set()
for i in range(m):
    operation = tuple(map(int, lines[i+2].rstrip().split()))
    operations.append(operation)
    if operation[0] == 3:
        interested.add(operation[1])
interested_list = list()
for item in interested:
    interested_list.append(item)
for operation in operations:
    if operation[0] == 1:
        array[operation[1]-1] = operation[2]
    if operation[0] == 2:
        for i in range(len(interested_list)):
            array[interested_list[i]-1] += operation[1]
    if operation[0] == 3:
        print(array[operation[1]-1])