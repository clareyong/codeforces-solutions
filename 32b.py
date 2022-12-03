borze = input()
output = ''

is_previous_was_dash = False
for c in borze:
    if is_previous_was_dash == True:
        if c == '.':
            output += '1'
        else: 
            output += '2'
        is_previous_was_dash = False
    else:
        if c == '-':
            is_previous_was_dash = True
        else:
            output += '0'

print(output)