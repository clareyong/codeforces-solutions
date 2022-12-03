s1 = input()
s2 = input()
list1 = list()
list2 = list()

for c in s1:
    if c != ' ':
        list1.append(c)
for c in s2:
    if c != ' ':
        list2.append(c)

flag = True
for c in list2:
    if c in list1:
        list1.pop(list1.index(c))
    else:
        flag = False
if flag == True:
    print("YES")
else:
    print("NO")