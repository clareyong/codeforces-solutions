boys, girls = map(int, input().split())
unit = 'BG'

if boys == girls:
    answer = unit * boys
elif boys > girls:
    answer = unit * girls + 'B' * (boys - girls)
elif girls > boys:
    answer = unit * boys + 'G' * (girls - boys)
else:
    print('')
print(answer)


# if boys == girls:
#     print(unit * boys)
# elif boys > girls:
#     print(unit * girls + 'B' * (boys - girls))
# elif girls > boys:
#     print(unit * boys + 'G' * (girls - boys))
