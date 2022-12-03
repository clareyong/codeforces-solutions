year = int(input()) + 1
next_year = -1

while next_year < 0:
    year_str = str(year)
    flag = True
    for i, n in enumerate(year_str):
        for j, m in enumerate(year_str):
            if i != j:
                if n == m:
                    flag &= False
                    break
                if n != m:
                    flag &= True
    if flag == True:
        next_year = year
    else:
        year += 1

print(next_year)

# year = int(input()) + 1

# while True:
#     year_str = str(year)
#     char_count = len(set(year_str))
#     if char_count == 4:
#         break
#     else: 
#         year += 1
# print(year)


