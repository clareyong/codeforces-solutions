number = int(input())
percentages = list(map(int, input().split()))
total = 0

for percentage in percentages:
    total += percentage

average = total / number
print(average)