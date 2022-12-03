number_of_people, front, back = map(int, input().split())
minimum = min(number_of_people - front, back + 1)     
print(minimum)