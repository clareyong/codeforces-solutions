initial, number_of_dragons = map(int, input().split())
dragon_strengths = list()
bonuses = list()
for i in range(number_of_dragons):
    dragon_strength, bonus = map(int, input().split())
    dragon_strengths.append(dragon_strength)
    bonuses.append(bonus)

for i in range(len(dragon_strengths)):
    initial -= dragon_strengths[i]
    if initial >= 0:
        initial += bonuses[i]

if initial >= 0:
    print('YES')
else:
    print('NO')
