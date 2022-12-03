word = input()

commands = ['H', 'Q', '9']

flag = False
for letter in word:
    if letter in commands:
        print('YES')
        flag = True
        break

if flag == False:
    print('NO')