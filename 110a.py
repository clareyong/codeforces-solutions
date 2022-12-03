numbers = input()
lucky_numbers = ['4', '7']

counter = 0
for number in numbers:
    if number in lucky_numbers:
        counter += 1

if counter == 4 or counter == 7:
    print('YES')
else:
    print('NO')

