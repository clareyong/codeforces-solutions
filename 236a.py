username = input()
letters = set()

for c in username:
    letters.add(c)

if len(letters) % 2:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")