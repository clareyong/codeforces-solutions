guest_name = input()
resident_host = input()
pile = input()

all_letters = []
pile_of_letters = []
for c in guest_name:
    all_letters.append(c)
for c in resident_host:
    all_letters.append(c)
for c in pile:
    pile_of_letters.append(c)

all_letters.sort()
pile_of_letters.sort()

if all_letters == pile_of_letters:
    print('YES')
else:
    print('NO')