number_of_digits = int(input())
number = input()
first_half = list()
second_half = list()

flag = False

for i in range(number_of_digits):
    first_half.append(int(number[i]))
for i in range(number_of_digits, (2*number_of_digits)):
    second_half.append(int(number[i]))
first_half.sort()
second_half.sort()

status = ''
if first_half[0] > second_half[0]:
    status = 'first_half'
elif second_half[0] > first_half[0]:
    status = 'second_half'
else:
    flag = False

for i in range(number_of_digits):
    if status == 'first_half':
        if first_half[i] > second_half[i]:
            flag = True
        else:
            flag = False
            break
    elif status == 'second_half':
        if first_half[i] < second_half[i]:
            flag = True
        else:
            flag = False
            break
if flag == False:    
    print('NO')
else:
    print('YES')