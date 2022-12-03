number = input()

flag = True
current = 'zero'
for c in number:
    # print('before', c, current)
    if c == '1':
        if current == 'zero':
            current = 'one'
        elif current == 'one':
            current = 'one'
        elif current == 'one_four':
            current = 'one'
        elif current == 'one_four_four':
            current = 'one'
        else:
            print('NO')
            flag = False
            break
    elif c == '4':
        if current == 'one':
            current = 'one_four'
        elif current == 'one_four':
            current = 'one_four_four'
        else:
            print('NO')
            flag = False
            break
    else:
        print('NO')
        flag = False
        break
    # print('after', c, current)
if flag == True:
    print('YES')


# 1
# 14
# 144    