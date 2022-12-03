number_of_stations = int(input())
boards = list()
alights = list()
for i in range(number_of_stations):
    alight, board = map(int, input().split())
    boards.append(board)
    alights.append(alight)

people = list()
initial = boards[0] + alights[0]
people.append(initial)
for i in range(1, len(boards)):
    curr_val = initial + boards[i] - alights[i]
    people.append(curr_val)
    initial = curr_val
print(max(people))


# for i in range(1, len(boards)):
#     print(maximum + boards[i] - alights[i])
#     if maximum + boards[i] - alights[i] > maximum:
#         maximum = maximum + boards[i] - alights[i]
# print(maximum)

# 11 9 7 12 12 12 18