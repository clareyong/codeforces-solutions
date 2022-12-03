n = int(input())
for i in range(n):
    people = int(input())
    direction = list(input())
    # print(people, direction)
    total = 0
    difference = list()
    for j in range(people):
        if direction[j] == 'L':
            total += j
            difference.append(people - j - 1 - j)
        else:
            total += people - j - 1
            difference.append(j - (people - j - 1))
        # print(total, difference)
    difference.sort(reverse=True)
    for item in difference:
        if item > 0:
            total += item
        print(total, end=' ')
    print('')
