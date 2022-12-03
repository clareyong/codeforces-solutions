number = int(input())
num_list = list()
new_number = number * 2
answer = ''
for i in range(number+1, new_number+1):
    print(i, end=' ')
# answer.rstrip()
# print(answer)

# def is_prime(number):
#     if number > 1:
#         for i in range(2, int(number/2)+1):
#             if number % i == 0:
#                 return False
#                 break
#         return True

# num = 2
# while len(num_list) < number:
#     if is_prime(num) == True:
#         num_list.append(num)
#         num += 1
#     else:
#         num += 1

# answer = ''
# for num in num_list:
#     answer += str(num) + ' '

# answer.rstrip()
# print(answer)
