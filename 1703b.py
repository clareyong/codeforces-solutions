number = int(input())
competitions = list()
for i in range(number):
    _ = input()
    solved = competitions.append(input())

from collections import defaultdict

for competition in competitions:
    winners = defaultdict(int)
    for c in competition:
        if c in winners.keys():
            winners[c] += 1
        else:
            winners[c] = 1
    # print(winners)
    counter = 0
    for key, item in winners.items():
        counter += item + 1
    print(counter)
