import sys

# s = sys.stdin.read().split('\n')
# number = s[0]
# words = s[1:]
# print(words)

words = []
number = int(input())
for i in range(number):
    words.append(input())

for word in words:
    word = word.lower()
    if word == 'yes':
        print("YES")
    else:
        print("NO")