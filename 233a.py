number = int(input())

if number % 2 == 1:
    print(-1)
else:
    num_list = list(range(1, number + 1))
    for i in range(0, number-1, 2):
        num_list[i], num_list[i+1] = num_list[i+1], num_list[i]
    answer = ''
    for num in num_list:
        answer += str(num) +' '
    answer.rstrip()
    print(answer)
