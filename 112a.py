string_1 = input().lower()
string_2 = input().lower()
ranks = []
for i in range(len(string_1)):
    if ord(string_1[i]) > ord(string_2[i]):
        ranks.append(1)
        break
    elif ord(string_1[i]) < ord(string_2[i]):
        ranks.append(-1)
        break

if len(ranks) != 0:
    print(ranks[0])
else:
    print(0)
