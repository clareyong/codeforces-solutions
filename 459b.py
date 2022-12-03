number_of_flowers = int(input())
beauties = list(map(int, input().split()))

maximum = max(beauties)
minimum = min(beauties)
max_count = 0
min_count = 0
for beauty in beauties:
    if beauty == maximum:
        max_count += 1
    if beauty == minimum:
        min_count += 1
difference = maximum - minimum
possibilities = max_count * min_count
if maximum == minimum:
        print(0, 1)
else:
    print(difference, possibilities)

# 1 3 1 3 1
# 12 14 23 34 25 45

# 1 3 1 3 1 3
# 1 2 3 4 5 6

# 12 14 16 23 34 36 25 45 56 

# 3 1 2 3 1
# 1 2 3 4 5

# 12 15 24 35