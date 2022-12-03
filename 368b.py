import sys

input_ = sys.stdin.read().split('\n')
n, m = map(int, input_[0].split())
# n, m = map(int, input().split())
numbers = list(map(int, input_[1].split()))
# print(numbers)
# numbers = list(map(int, input().split()))
counter = list()
number_set = set()
for i in reversed(range(n)):
    # print(i)
    if numbers[i] not in number_set:
        number_set.add(numbers[i])
    counter.append(len(number_set))
counter.reverse()
# print(counter)

for i in range(2,len(input_)):
    if input_[i] != '':
        print(counter[int(input_[i])-1])

